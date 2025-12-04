from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///data.db", echo=True)
base = declarative_base()

class film(base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    note = Column(Float, nullable=False)

base.metadata.create_all(engine)