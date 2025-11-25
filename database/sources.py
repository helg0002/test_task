from sqlalchemy import (
    String,
    Integer
)
from sqlalchemy.orm import mapped_column, Session, Mapped

from .db import Base, Session


class SourceTable(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    @staticmethod
    def insert(name: str) -> "SourceTable":
        with Session() as session:
            source = SourceTable(
                name=name,
            )
            session.add(source)
            session.commit()
            session.refresh(source)
            return source

    @staticmethod
    def get_row(source_id: int) -> "SourceTable":
        with Session() as session:
            return session.query(SourceTable).filter_by(id=source_id).first()

    @staticmethod
    def get_row_all() -> list["SourceTable"]:
        with Session() as session:
            return session.query(SourceTable).all()

    # @staticmethod
    # def delete(user_hash: str):
    #     with Session(bind=engine) as session:
    #         query = session.query(Presets).where(user_hash == Presets.user_hash).first()
    #         session.delete(query)
    #         session.commit()
