from sqlalchemy import Column, Integer, String, Date, Boolean
from db import Base

class Samochod(Base):
    __tablename__ = 'samochod'

    id = Column(Integer, primary_key=True)
    marka = Column(String(20))
    rok_produkcji = Column(Integer)
    model = Column(String(30))
