from typing import  Any

from sqlalchemy import (
    String,
    Boolean,
    Integer
)
from sqlalchemy.orm import mapped_column, Session, Mapped

from .db import Base, Session


class OperatorTable(Base):
    __tablename__ = "operators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    alive: Mapped[bool] = mapped_column(Boolean, default=True)
    limit: Mapped[int] = mapped_column(Integer, nullable=False)
    active_contacts: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    @staticmethod
    def insert(name: str, alive: bool, limit: int) -> "OperatorTable":
        with Session() as session:
            operator = OperatorTable(
                name=name,
                alive=alive,
                limit=limit
            )
            session.add(operator)
            session.commit()
            session.refresh(operator)
            return operator

    @staticmethod
    def get_row(operator_id: int) -> "OperatorTable":
        with Session() as session:
            return session.query(OperatorTable).filter_by(id=operator_id).first()

    @staticmethod
    def get_row_all() -> list["OperatorTable"]:
        with Session() as session:
            return session.query(OperatorTable).all()

    @staticmethod
    def update(operator_id: int, key: str, value: Any) -> None:
        with Session() as session:
            operator = session.query(OperatorTable).filter_by(id=operator_id).first()
            if operator is None:
                return
            setattr(operator, key, value)
            session.commit()

    @staticmethod
    def increment_active_contacts(operator_id: int) -> "OperatorTable":
        with Session() as session:
            operator = session.query(OperatorTable).filter_by(id=operator_id).first()
            if operator:
                operator.active_contacts += 1
                session.commit()
                session.refresh(operator)
                return operator

    # @staticmethod
    # def delete(user_hash: str):
    #     with Session(bind=engine) as session:
    #         query = session.query(Presets).where(user_hash == Presets.user_hash).first()
    #         session.delete(query)
    #         session.commit()
