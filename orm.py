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

def film_add(name, year, note):
    Session = sessionmaker(bind=engine)
    session = Session()
    films = film(name=name, year=year, note=note)
    session.add(films)
    session.commit()
    session.close()

film_add("TRON : Ares", 2025, 8.4)
film_add("Black Phone 2", 2025, 8.3)