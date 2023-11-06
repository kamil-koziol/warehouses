from sqlalchemy import Column, Integer, String, Date, Boolean
from db import Base

class Krusant(Base):
    __tablename__ = 'krusant'

    id = Column(Integer, primary_key=True)
    imie = Column(String(20))
    nazwisko = Column(String(30))
    pesel = Column(String(11))
    data_urodzenia = Column(Date)
    plec = Column(Boolean)
