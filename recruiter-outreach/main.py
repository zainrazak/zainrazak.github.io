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
