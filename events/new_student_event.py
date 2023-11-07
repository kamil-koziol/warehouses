import random
from typing import List

from sqlalchemy import null

from db import *
from db.scripts import *
from simulation_properties import *
from .simulation_event import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime


def get_instructor_with_less_hrs(session):
    instructors = session.query(Instruktor).all()
    for ins in sorted(instructors, key=lambda x: x.number_of_active_courses):
        if ins.data_zwolnienia != null:
            return ins


class NewStudentEvent(SimulationEvent):
    @staticmethod
    def run(session: Session, day: datetime):
        if get_number_of_active_courses(session) < MAX_AMOUNT_OF_STUDENTS:
            instructor = get_instructor_with_less_hrs(session)
            new_student = Krusant.get_random(day)

            kurs = Kurs()
            kurs.data_rozpoczecia = day
            kurs.ko_kursant_id = new_student.id
            kurs.ko_instruktor_id = instructor.id
            instructor.number_of_active_courses += 1
            session.add(new_student)
            session.add(kurs)
            if DEBUG_MODE:
                print("Dodano kursanta:" + new_student.to_string() + " do instruktora:" + instructor.to_string())
