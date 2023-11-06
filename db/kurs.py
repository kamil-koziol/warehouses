from sqlalchemy import Column, Integer, String, Date, Boolean
from db import Base

class Kurs(Base):
    __tablename__ = 'kurs'

    id = Column(Integer, primary_key=True)
    ko_kursant_id = Column(Integer, ForeignKey('krusant.id'))
    ko_instruktor_id = Column(Integer, ForeignKey('instruktor.id'))
    data_rozpoczecia = Column(Date)
    data_zakonczenia = Column(Date, nullable=True)
