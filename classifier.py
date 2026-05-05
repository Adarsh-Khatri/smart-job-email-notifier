def is_job_mail(subject, sender):
    subject = subject.lower()
    sender = sender.lower()

    # ❌ BLOCK system / unwanted senders
    blocked_senders = [
        "github.com",
        "notifications@",
        "no-reply",
        "noreply",
        "mailer-daemon",
    ]

    if any(b in sender for b in blocked_senders):
        return False

    # ❌ BLOCK GitHub-related subjects
    if "github" in subject or "workflow" in subject:
        return False

    # ✅ ONLY ALLOW trusted job sources (IMPORTANT 🔥)
    trusted_sources = [
        "naukri",
        "linkedin",
        "internshala",
        "indeed",
        "glassdoor"
    ]

    if not any(src in sender for src in trusted_sources):
        return False   # 🔥 strict filtering

    # ✅ job keywords
    keywords = [
        "job", "internship", "hiring", "career",
        "opportunity", "opening", "vacancy",
        "walk-in", "recruitment", "apply now"
    ]

    return any(word in subject for word in keywords)