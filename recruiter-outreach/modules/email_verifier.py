"""
email_verifier.py — Verify email deliverability for a list of contacts via Hunter.io.

Public interface:
    verify_contacts(contacts: list[dict]) -> list[dict]

Flow:
    1. For each contact, check if Apollo email_confidence > 85
       -> if so, skip Hunter verification and mark as verified
    2. Otherwise, GET https://api.hunter.io/v2/email-verifier
       with the contact's email address
    3. Extract: result, score, deliverability, mx_records, smtp_check
    4. Filter out contacts where deliverability == "undeliverable"
    5. Sort remaining contacts by confidence score descending
    6. Return cleaned, verified contact list

Returns the same contact list schema from contact_finder, extended with:
    {
        ...all previous fields...,
        "hunter_score": int,
        "deliverability": str,      # "deliverable" / "risky" / "undeliverable"
        "verified": bool
    }

Raises:
    RuntimeError if the Hunter API call fails unexpectedly.
"""
