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

# film_add("TRON : Ares", 2025, 8.4)
# film_add("Black Phone 2", 2025, 8.3)

def film_atualize(id, name=None, year=None, note=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    films = session.query(film).filter_by(id=id).first()
    if films:
        if name is not None:
            films.name = name
        if year is not None:
            films.year = year
        if note is not None:
            films.note = note
        session.commit()
    session.close()

# film_atualize(1,"Sarah's Oil", 2025, 9.8)

def film_delete(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    films = session.query(film).filter_by(id=id).first()
    if films:
        session.delete(films)
    session.commit()
    session.close()

film_delete(2)