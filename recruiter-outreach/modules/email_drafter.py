"""
email_drafter.py — Draft a personalized cold outreach email via Claude API.

Public interface:
    draft_email(job_data: dict, contact: dict) -> dict

Flow:
    1. Load system prompt from prompts/email_draft_prompt.txt
    2. Inject runtime variables into the prompt:
       {{role_title}}, {{company_name}}, {{contact_name}},
       {{department}}, {{seniority}}
    3. Call Claude API (claude-sonnet-4-6) with the populated prompt
    4. Parse the JSON response: {"subject": str, "body": str}
    5. Return the dict

Returns:
    {
        "subject": str,     # Specific subject line for the role
        "body": str         # Max 150-word email body
    }

Raises:
    ValueError if Claude returns malformed JSON.
    RuntimeError if the API call fails.
"""
