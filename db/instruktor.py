from sqlalchemy import Column, Integer, String, Date, Boolean
from db import Base

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
