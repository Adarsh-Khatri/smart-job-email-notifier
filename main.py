import json
import os
from email_reader import authenticate_gmail, get_emails
from classifier import is_job_mail
from telegram import send_to_telegram

PROCESSED_FILE = "processed_emails.json"


def load_processed():
    if not os.path.exists(PROCESSED_FILE):
        return set()
    with open(PROCESSED_FILE, "r") as f:
        return set(json.load(f))


def save_processed(processed_ids):
    with open(PROCESSED_FILE, "w") as f:
        json.dump(list(processed_ids), f)


def main():
    service = authenticate_gmail()
    emails = get_emails(service, max_results=20)

    processed_ids = load_processed()

    for email in emails:

        subject = email['subject'].lower()
        sender = email['sender'].lower()

        # HARD BLOCK BEFORE ANYTHING
        if "github" in sender:
            print("Skipped GitHub email:", subject)
            continue

        if "notification" in sender or "noreply" in sender:
            print("Skipped system email:", subject)
            continue

        # ✅ now apply job filter
        if is_job_mail(subject, sender):
            message = f"🚀 Job Alert!\n\n{email['subject']}\nFrom: {email['sender']}"
            send_to_telegram(message)

    save_processed(processed_ids)


if __name__ == "__main__":
    main()