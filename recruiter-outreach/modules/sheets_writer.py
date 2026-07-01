"""
sheets_writer.py — Log pipeline output to a Google Sheet via gspread.

Public interface:
    write_to_sheet(job_data: dict, contacts: list[dict], draft: dict | None = None) -> None
    update_outreach_status(job_url: str, status: str, sent_at: str | None = None) -> None

Flow (write_to_sheet):
    1. Auth via Google Service Account JSON
       (path from GOOGLE_SHEETS_CREDENTIALS_PATH env var)
    2. Open the sheet by GOOGLE_SHEET_ID, tab named "Pipeline"
    3. Create header row automatically if the sheet is empty
    4. Check for existing row matching job_url -> skip if found (dedup)
    5. Write one row per contact with all pipeline fields

Sheet columns (A-R):
    A: Timestamp
    B: Company Name
    C: Role Title
    D: Department
    E: Seniority
    F: Location
    G: Remote Type
    H: Job URL
    I: ATS Platform
    J: Contact Name
    K: Contact Title
    L: Contact LinkedIn
    M: Contact Email
    N: Email Confidence Score
    O: Verified (TRUE/FALSE)
    P: Outreach Status  (default: "Pending")
    Q: Email Draft
    R: Notes

Flow (update_outreach_status):
    Find the row(s) matching job_url and update column P (and optionally R).
"""
