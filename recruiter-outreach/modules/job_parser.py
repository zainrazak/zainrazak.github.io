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
