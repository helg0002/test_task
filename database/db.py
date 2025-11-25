from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

from cfg import config


engine = create_engine(
    config.database.url
)

meta = MetaData()
meta.reflect(bind=engine)
Base = declarative_base()
Session = sessionmaker(bind=engine)