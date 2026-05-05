def is_job_mail(subject, sender):
    keywords = [
        "job", "internship", "hiring", "career",
        "opportunity", "opening", "vacancy",
        "walk-in", "recruitment", "apply now"
    ]
    text = (subject + " " + sender).lower()

    return any(word in text for word in keywords)