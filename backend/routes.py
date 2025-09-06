from fastapi import APIRouter
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import Email, DraftResponse
from .email_client import fetch_emails, send_email

router = APIRouter()

# Fetch real emails and store in DB
@router.post("/fetch_emails")
def fetch_and_store_emails(limit: int = 10):
    db: Session = SessionLocal()
    try:
        emails = fetch_emails(limit=limit)
        count = 0
        for e in emails:
            email_obj = Email(
                sender=e["sender"],
                subject=e.get("subject", ""),
                body=e.get("body", "")
            )
            db.add(email_obj)
            count += 1
        db.commit()
        return {"status": "success", "emails_fetched": count}
    except Exception as ex:
        return {"status": "error", "detail": str(ex)}
    finally:
        db.close()

# Send a draft reply to an email
@router.post("/send_draft/{email_id}")
def send_draft(email_id: int, draft_body: str):
    db: Session = SessionLocal()
    try:
        email_obj = db.query(Email).filter(Email.id == email_id).first()
        if not email_obj:
            return {"status": "error", "detail": "Email not found"}

        send_email(email_obj.sender, email_obj.subject or "Re: Your email", draft_body)

        draft = DraftResponse(email_id=email_obj.id, draft=draft_body)
        db.add(draft)
        email_obj.resolved = True
        db.commit()
        return {"status": "success", "detail": "Draft sent successfully!"}
    except Exception as ex:
        return {"status": "error", "detail": str(ex)}
    finally:
        db.close()
