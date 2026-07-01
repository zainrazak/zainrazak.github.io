# Recruiter Outreach Automation — Claude Session Context

## What This Project Is

A fully automated recruiter outreach pipeline. Zain pastes a job posting URL, the system:
1. Scrapes and parses the job via Claude API → structured JSON
2. Finds recruiters at that company via Apollo.io API
3. Verifies email deliverability via Hunter.io
4. Logs everything to a Google Sheet tracker
5. Drafts a personalized cold email via Claude API
6. Displays the draft in a web UI for review → sends via Gmail on approval

**The only manual steps are:** pasting the URL + approving the email before send.

---

## Who This Is For

**Zain Razak** — Data & AI Product Manager and Consultant at Accenture Strategy & Consulting.
Experience at Disney Imagineering, Capital Group, Google.
Certifications: Scrum Master, Salesforce Admin, AWS AI, Google Cloud.
Actively exploring Senior PM / TPM / AI Product roles.

---

## Project Location

```
~/recruiter-outreach/
```

This folder already exists on your Mac and is fully set up.

---

## Current File Structure

```
recruiter-outreach/
├── .env                          ← API keys (already filled in: ANTHROPIC_API_KEY)
├── .env.example                  ← Template showing all required keys
├── .gitignore
├── README.md
├── CLAUDE.md                     ← This file
├── requirements.txt              ← All deps installed in .venv
├── app.py                        ← Flask web UI (run this to use the app)
├── main.py                       ← CLI entry point (legacy, use app.py instead)
├── .venv/                        ← Python virtual environment (already created)
├── modules/
│   ├── __init__.py
│   ├── job_parser.py             ← BUILT & WORKING ✅
│   ├── contact_finder.py         ← Scaffold only, not built yet
│   ├── email_verifier.py         ← Scaffold only, not built yet
│   ├── sheets_writer.py          ← Scaffold only, not built yet
│   └── email_drafter.py          ← Scaffold only, not built yet
├── prompts/
│   ├── job_parser_prompt.txt     ← System prompt for job parsing (done)
│   └── email_draft_prompt.txt    ← System prompt for email drafting (done)
└── cache/
    └── .gitkeep                  ← SQLite cache will go here
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Runtime |
| Flask | Web UI server |
| Claude API (`claude-sonnet-4-6`) | Job parsing + email drafting |
| Apollo.io API | Recruiter/contact discovery |
| Hunter.io API | Email verification |
| Google Sheets API (gspread) | Pipeline logging |
| Gmail SMTP | Email send after approval |
| SQLite | Local cache (avoid re-querying same companies) |
| BeautifulSoup4 + Requests | Job page scraping |
| Rich | CLI formatting |

---

## Environment Setup (Already Done)

```bash
cd ~/recruiter-outreach
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### API Keys in .env

- `ANTHROPIC_API_KEY` — ✅ filled in
- `APOLLO_API_KEY` — needed for Phase 3
- `HUNTER_API_KEY` — needed for Phase 4
- `GOOGLE_SHEETS_CREDENTIALS_PATH` — needed for Phase 5
- `GOOGLE_SHEET_ID` — needed for Phase 5
- `GMAIL_ADDRESS` — needed for Phase 8
- `GMAIL_APP_PASSWORD` — needed for Phase 8

---

## How to Start the App

```bash
cd ~/recruiter-outreach
source .venv/bin/activate
python app.py
```

Then open **http://localhost:8080** in your browser.

> Note: Port 5000 conflicts with macOS AirPlay. We use 8080.

---

## What's Built and Working

### ✅ Phase 1 — Scaffold
All files created with docstrings, requirements.txt, .env.example, .gitignore, README.

### ✅ Phase 2 — job_parser.py
- Accepts a job URL
- Scrapes page text with requests + BeautifulSoup
- Sends to Claude API with structured prompt
- Returns clean JSON

**Tested successfully** with:
`https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6016320004`

Output:
```json
{
  "company_name": "Sony Interactive Entertainment (PlayStation)",
  "company_domain": "sie.com",
  "role_title": "Staff Technical Project Manager",
  "department": "Technical Operations",
  "seniority": "Staff",
  "location": "Aliso Viejo, CA, United States",
  "remote_type": "Hybrid",
  "ats_platform": "Greenhouse",
  "job_id": null,
  "job_url": "https://...",
  "raw_description": "..."
}
```

### ✅ Flask Web UI (app.py + templates/index.html)
- Dark, clean single-page UI
- Paste a URL → click Run Pipeline
- Live progress steps (1–5) with status indicators
- Step 1 (job parse) completes and shows a Job Details card
- Steps 2–5 show "coming soon" until built
- Runs at http://localhost:8080

---

## What Needs to Be Built Next

### Phase 3 — contact_finder.py
- Input: job_data dict from job_parser
- POST to Apollo.io `/v1/mixed_people/search`
- Filter by recruiter/TA titles at the company domain
- Cache results in SQLite (cache/contacts.db, 30-day TTL)
- Return top 3 contacts ranked by relevance
- Wire into app.py Step 2

**Apollo API details:**
- Endpoint: `POST https://api.apollo.io/v1/mixed_people/search`
- Auth: `x-api-key` header
- Key params: `organization_domains`, `person_titles`, `per_page: 10`

Output schema:
```json
[{
  "full_name": "Jane Smith",
  "title": "Senior Technical Recruiter",
  "linkedin_url": "https://linkedin.com/in/...",
  "email": "jane@company.com",
  "email_confidence": 92,
  "apollo_id": "abc123"
}]
```

### Phase 4 — email_verifier.py
- Input: contacts list from contact_finder
- GET Hunter.io `/v2/email-verifier` for each contact
- Skip verification if Apollo confidence > 85
- Filter out undeliverable emails
- Sort by confidence score
- Wire into app.py Step 3

### Phase 5 — sheets_writer.py
- Auth via Google Service Account JSON
- Write one row per contact to "Pipeline" tab
- Columns A–R (Timestamp → Notes)
- Dedup by job_url
- Wire into app.py Step 4

### Phase 6 — email_drafter.py
- Input: job_data + top contact
- Inject variables into prompts/email_draft_prompt.txt
- Call Claude API → returns `{"subject": str, "body": str}`
- Wire into app.py Step 5
- Show draft in UI with Edit / Approve / Skip buttons

### Phase 7 — Full pipeline orchestration in app.py
- Connect all 5 steps end to end
- Add approve/edit/skip UI for email draft
- Update Sheet status on send/skip

### Phase 8 — Gmail send
- smtplib + SMTP with Gmail app password
- Send approved email
- BCC Zain for records
- Log send timestamp back to Sheet

---

## Known Issues / Notes

- LinkedIn URLs don't work for scraping (requires login). Use direct job board URLs:
  - Greenhouse: `boards.greenhouse.io/...`
  - Lever: `jobs.lever.co/...`
  - Workday: `company.wd5.myworkdayjobs.com/...`
- Port 5000 blocked by macOS AirPlay — always use 8080
- The scraping must run locally (cloud container's proxy blocks external URLs)
- `.env` is gitignored — never push API keys

---

## GitHub

**Repo:** `zainrazak/zainrazak.github.io`
**Branch:** `claude/recruiter-outreach-scaffold-78xdu5`

To pull latest:
```bash
cd ~/zainrazak.github.io && git pull origin claude/recruiter-outreach-scaffold-78xdu5
cp -r recruiter-outreach/. ~/recruiter-outreach/
```

---

## Build Order for Next Session

1. Add `APOLLO_API_KEY` to `~/recruiter-outreach/.env`
2. Build `modules/contact_finder.py` (Phase 3)
3. Test contact_finder with Sony PlayStation job data
4. Wire Step 2 into app.py and test in browser
5. Then proceed to Phase 4 (email_verifier.py)
