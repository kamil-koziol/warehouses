import uuid

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Uuid

import simulation_properties
from db import Base
from dataclasses import dataclass

@dataclass
class Kurs(Base):
    __tablename__ = 'kurs'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    ko_kursant_id = Column(Uuid, ForeignKey('krusant.id'))
    ko_instruktor_id = Column(Uuid, ForeignKey('instruktor.id'))
    data_rozpoczecia = Column(Date)
    data_zakonczenia = Column(Date, nullable=True)

    hours_remaining = simulation_properties.HOURS_IN_COURSE

    def finish_course(selfself,session):
        pass