import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

engine = sqlalchemy.create_engine("sqlite:///db.sqlite", echo=False)
Base = sqlalchemy.orm.declarative_base()

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  # once engine is available

session = Session()

class Instruktor(Base):
    __tablename__ = 'instruktor'
    
    id = Column(Integer, primary_key=True)
    imie = Column(String(20))
    nazwisko = Column(String(30))
    pesel = Column(String(11))
    poczatek_pracy = Column(Integer)
    data_urodzenia = Column(Date)
    data_zatrudnienia = Column(Date)
    plec = Column(Boolean)

class Krusant(Base):
    __tablename__ = 'krusant'
    
    id = Column(Integer, primary_key=True)
    imie = Column(String(20))
    nazwisko = Column(String(30))
    pesel = Column(String(11))
    data_urodzenia = Column(Date)
    plec = Column(Boolean)

class Kurs(Base):
    __tablename__ = 'kurs'
    
    id = Column(Integer, primary_key=True)
    ko_kursant_id = Column(Integer, ForeignKey('krusant.id'))
    ko_instruktor_id = Column(Integer, ForeignKey('instruktor.id'))
    data_rozpoczecia = Column(Date)
    data_zakonczenia = Column(Date, nullable=True)

class Zajecia(Base):
    __tablename__ = 'zajecia'
    
    id = Column(Integer, primary_key=True)
    ko_kurs_id = Column(Integer, ForeignKey('kurs.id'))
    ko_samochod_id = Column(Integer, ForeignKey('samochod.id'))
    poczatek = Column(DateTime)
    koniec = Column(DateTime)
    sie_odbyly = Column(Boolean)

class Samochod(Base):
    __tablename__ = 'samochod'
    
    id = Column(Integer, primary_key=True)
    marka = Column(String(20))
    rok_produkcji = Column(Integer)
    model = Column(String(30))

class DaneUdostepnionePrzezWORD(Base):
    __tablename__ = 'dane_udostepnione_przez_word'
    
    id = Column(Integer, primary_key=True)
    zdano = Column(Boolean)
    data_czas_egzaminu = Column(DateTime)

Base.metadata.create_all(engine)
