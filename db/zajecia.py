from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from db import Base

class Zajecia(Base):
    __tablename__ = 'zajecia'

    id = Column(Integer, primary_key=True)
    ko_kurs_id = Column(Integer, ForeignKey('kurs.id'))
    ko_samochod_id = Column(Integer, ForeignKey('samochod.id'))
    poczatek = Column(DateTime)
    koniec = Column(DateTime)
    sie_odbyly = Column(Boolean)
