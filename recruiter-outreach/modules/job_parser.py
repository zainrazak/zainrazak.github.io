"""
job_parser.py — Scrape a job posting URL and extract structured data via Claude API.

Public interface:
    parse_job(url: str) -> dict

Flow:
    1. Fetch raw HTML from the job URL using requests
    2. Extract visible text with BeautifulSoup
    3. Send text to Claude API with the system prompt from
       prompts/job_parser_prompt.txt
    4. Parse and return the JSON response

Returns a dict matching this schema:
    {
        "company_name": str,
        "company_domain": str,      # e.g. "capitalgroup.com"
        "role_title": str,
        "department": str,
        "seniority": str,           # Junior / Mid / Senior / Staff / Principal / Director / VP / C-Level
        "location": str,
        "remote_type": str,         # Remote / Hybrid / Onsite / Unknown
        "ats_platform": str,        # Workday / Greenhouse / Lever / iCIMS / Taleo / Unknown
        "job_id": str | None,
        "job_url": str,
        "raw_description": str      # First 500 chars of the posting
    }

Raises:
    ValueError if the page cannot be fetched or Claude returns unparseable JSON.
"""

import json
import os
from pathlib import Path

import anthropic
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def _load_prompt() -> str:
    return (PROMPTS_DIR / "job_parser_prompt.txt").read_text()


def _scrape(url: str) -> str:
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ValueError(f"Failed to fetch job URL: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    lines = [line for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def _parse_with_claude(page_text: str, url: str) -> dict:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    system_prompt = _load_prompt()

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"{system_prompt}\n\n{page_text[:8000]}",
            }
        ],
    )

    raw = message.content[0].text.strip()

    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Claude returned invalid JSON: {e}\n\nRaw response:\n{raw}")

    result["job_url"] = url
    return result


def parse_job(url: str) -> dict:
    """Scrape a job posting URL and return structured data via Claude API."""
    page_text = _scrape(url)
    return _parse_with_claude(page_text, url)
