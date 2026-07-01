"""
main.py — CLI entry point for the recruiter outreach pipeline.

Usage:
    python main.py --url "https://linkedin.com/jobs/view/..."

Flow:
    1. Parse job posting URL → structured job data (job_parser)
    2. Find recruiter contacts at the company (contact_finder)
    3. Verify email deliverability (email_verifier)
    4. Log everything to Google Sheets (sheets_writer)
    5. Draft personalized outreach email (email_drafter)
    6. Prompt user to review → send via Gmail on approval

Environment:
    All API keys loaded from .env via python-dotenv.
"""

import argparse

from dotenv import load_dotenv
from rich import print_json
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()


def main():
    parser = argparse.ArgumentParser(description="Recruiter outreach pipeline")
    parser.add_argument("--url", required=True, help="Job posting URL")
    args = parser.parse_args()

    # Phase 2: job_parser
    from modules.job_parser import parse_job

    console.print(Panel("[bold cyan]Step 1 — Parsing job posting...[/bold cyan]"))
    job_data = parse_job(args.url)
    console.print(Panel("[bold green]Job parsed successfully[/bold green]"))
    print_json(data=job_data)


if __name__ == "__main__":
    main()
