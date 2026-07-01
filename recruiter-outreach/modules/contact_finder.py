"""
contact_finder.py — Find recruiter/hiring manager contacts at a company via Apollo.io API.

Public interface:
    find_contacts(job_data: dict) -> list[dict]

Flow:
    1. Check SQLite cache (cache/contacts.db) for recent results
       for the same company_domain (< 30 days old) → return cached if found
    2. POST to Apollo /v1/mixed_people/search filtered by:
       - organization_domains: [company_domain]
       - person_titles: ["recruiter", "talent acquisition", "technical recruiter", "TA"]
    3. Rank results by title relevance to the role
    4. Cache the results with a timestamp
    5. Return top 3 contacts

Returns a list of dicts matching this schema:
    [
        {
            "full_name": str,
            "title": str,
            "linkedin_url": str,
            "email": str | None,
            "email_confidence": int,    # 0-100
            "apollo_id": str
        }
    ]

Raises:
    RuntimeError if the Apollo API call fails.
"""
