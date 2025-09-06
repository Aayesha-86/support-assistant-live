from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    body = Column(Text, nullable=False)
    received_at = Column(DateTime, default=datetime.utcnow)
    resolved = Column(Boolean, default=False)

    drafts = relationship("DraftResponse", back_populates="email")

class DraftResponse(Base):
    __tablename__ = "draft_responses"

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(Integer, ForeignKey("emails.id"), nullable=False)
    draft = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    email = relationship("Email", back_populates="drafts")
