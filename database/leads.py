from typing import Type
from sqlalchemy import (
    Integer,
    String
)
from sqlalchemy.orm import mapped_column, Session, Mapped

from .db import Base, Session


class LeadTable(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    external_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    @staticmethod
    def insert(external_id: str) -> "LeadTable":
        with Session() as session:
            lead = LeadTable(
                external_id=external_id
            )
            session.add(lead)
            session.commit()
            session.refresh(lead)
            return lead

    @staticmethod
    def get_row(external_id: str) -> "LeadTable":
        with Session() as session:
            return session.query(LeadTable).filter_by(external_id=external_id).first()



    # @staticmethod
    # def delete(user_hash: str):
    #     with Session(bind=engine) as session:
    #         query = session.query(Presets).where(user_hash == Presets.user_hash).first()
    #         session.delete(query)
    #         session.commit()
