import uuid

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Uuid
from sqlalchemy.orm import Session

import simulation_properties
from db import Base, Instruktor, Krusant
from dataclasses import dataclass


class Kurs(Base):
    __tablename__ = 'kurs'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    ko_kursant_id = Column(Uuid, ForeignKey('krusant.id'))
    ko_instruktor_id = Column(Uuid, ForeignKey('instruktor.id'))
    data_rozpoczecia = Column(Date)
    data_zakonczenia = Column(Date, nullable=True)
    hours_remaining = Column(Integer, default=simulation_properties.HOURS_IN_COURSE)

    def finish_course(self, session:Session, day):
        self.data_zakonczenia = day
        ins = session.query(Instruktor).get(self.ko_instruktor_id)
        ins.number_of_active_courses -= 1

        if simulation_properties.DEBUG_MODE:
            c = session.query(Krusant).get(self.ko_kursant_id)
            print(c.to_string() + " zakończył kurs")
