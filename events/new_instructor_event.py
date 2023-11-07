from db import *
from db.scripts import get_number_of_active_instructors
from simulation_properties import *
from .simulation_event import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime


class NewInstructorEvent(SimulationEvent):
    @staticmethod
    def run(session: Session, day: datetime):
        if get_number_of_active_instructors(session) < MAX_AMOUNT_OF_INSTRUCTORS:
            instructor = Instruktor.get_random(day)
            session.add(instructor)
            if VERBOSE:
                print("Dodano instruktora:" + instructor.to_string())
