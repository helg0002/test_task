from sqlalchemy import (
    Integer, ForeignKey
)
from sqlalchemy.orm import mapped_column, Session, Mapped, relationship

from .db import Base, Session


class SOWTable(Base):
    __tablename__ = "source_operator_weights"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    source_id: Mapped[int] = mapped_column(Integer, ForeignKey("sources.id"), nullable=False)
    operator_id: Mapped[int] = mapped_column(Integer, ForeignKey("operators.id"), nullable=False)
    weight: Mapped[int] = mapped_column(Integer, nullable=False)
    source = relationship("SourceTable")
    operator = relationship("OperatorTable")

    @staticmethod
    def insert(source_id: int, operator_id: int, weight: int) -> "SOWTable":
        with Session() as session:
            sow = SOWTable(
                source_id=source_id,
                operator_id=operator_id,
                weight=weight
            )
            session.add(sow)
            session.commit()
            session.refresh(sow)
            return sow

    @staticmethod
    def get_row_by_id_all(source_id: int) -> list["SOWTable"]:
        with Session() as session:
            return session.query(SOWTable).filter_by(source_id=source_id).all()

    @staticmethod
    def delete(source_id: int):
        with Session() as session:
            query = session.query(SOWTable).filter_by(source_id=source_id).delete()
            session.commit()
