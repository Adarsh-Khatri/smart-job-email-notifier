def is_job_mail(subject, sender):
    subject = subject.lower()
    sender = sender.lower()
    
    if "github" in subject:
        return False

    # ❌ ignore system emails
    ignore_sources = [
        "github.com",
        "notifications@",
        "no-reply",
        "noreply"
    ]

    for src in ignore_sources:
        if src in sender:
            return False

    # ✅ job-related keywords
    keywords = [
        "job", "internship", "hiring", "career",
        "opportunity", "opening", "vacancy",
        "walk-in", "recruitment", "apply now"
    ]

    return any(word in subject for word in keywords)