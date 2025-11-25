from datetime import datetime, UTC
from sqlalchemy import (
    Boolean,
    Integer,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import mapped_column, Session, Mapped, relationship

from .db import Base, Session


class ContactsTable(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lead_id: Mapped[int] = mapped_column(Integer, ForeignKey("leads.id"), nullable=False)
    source_id: Mapped[int] = mapped_column(Integer, ForeignKey("sources.id"), nullable=False)
    operator_id: Mapped[int] = mapped_column(Integer, ForeignKey("operators.id"), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    lead = relationship("LeadTable")
    source = relationship("SourceTable")
    operator = relationship("OperatorTable")

    @staticmethod
    def insert(lead_id: int, source_id: int, operator_id: int) -> "ContactsTable":
        with (Session() as session):
            contacts = ContactsTable(
                lead_id=lead_id,
                source_id=source_id,
                operator_id=operator_id
            )
            session.add(contacts)
            session.commit()
            session.refresh(contacts)
            return contacts



    # @staticmethod
    # def delete(user_hash: str):
    #     with Session(bind=engine) as session:
    #         query = session.query(Presets).where(user_hash == Presets.user_hash).first()
    #         session.delete(query)
    #         session.commit()
