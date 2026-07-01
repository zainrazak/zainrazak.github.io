# Recruiter Outreach Automation

Automated pipeline that turns a job posting URL into a personalized, verified outreach email — with one-click send after manual review.

## What it does

1. Paste a job URL → scrapes and parses the posting via Claude API
2. Finds recruiters/TA contacts at the company via Apollo.io
3. Verifies email deliverability via Hunter.io
4. Logs everything to a Google Sheet tracker
5. Drafts a personalized cold email via Claude API
6. Prompts you to review → sends via Gmail on approval

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Fill in your API keys in .env
```

## Usage

```bash
python main.py --url "https://linkedin.com/jobs/view/..."
```

## Module Overview

| Module | Purpose |
|---|---|
| `job_parser.py` | Scrape job URL → structured JSON via Claude API |
| `contact_finder.py` | Apollo API → find recruiters for that company |
| `email_verifier.py` | Hunter.io → verify email deliverability |
| `sheets_writer.py` | Log pipeline output to Google Sheets |
| `email_drafter.py` | Claude API → draft personalized outreach email |

## API Keys Required

- `ANTHROPIC_API_KEY` — console.anthropic.com
- `APOLLO_API_KEY` — app.apollo.io → Settings → API
- `HUNTER_API_KEY` — hunter.io → Dashboard → API
- `GOOGLE_SHEETS_CREDENTIALS_PATH` — Google Cloud Console Service Account JSON
- `GOOGLE_SHEET_ID` — from your Google Sheet URL
- `GMAIL_ADDRESS` + `GMAIL_APP_PASSWORD` — Google Account → Security → App Passwords
