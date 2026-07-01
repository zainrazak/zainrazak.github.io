"""
modules/ — Core pipeline modules for recruiter outreach automation.

Modules:
    job_parser      — Scrape + parse a job URL into structured JSON
    contact_finder  — Find recruiters at the target company via Apollo API
    email_verifier  — Verify email deliverability via Hunter.io
    sheets_writer   — Log pipeline output to a Google Sheet
    email_drafter   — Draft a personalized cold email via Claude API
"""
