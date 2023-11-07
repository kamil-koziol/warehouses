from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey

import simulation_properties
from db import Base
from dataclasses import dataclass

@dataclass
class Kurs(Base):
    __tablename__ = 'kurs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ko_kursant_id = Column(Integer, ForeignKey('krusant.id'))
    ko_instruktor_id = Column(Integer, ForeignKey('instruktor.id'))
    data_rozpoczecia = Column(Date)
    data_zakonczenia = Column(Date, nullable=True)

    hours_remaining = simulation_properties.HOURS_IN_COURSE
