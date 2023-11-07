from db import *
from simulation_properties import *
from .simulation_event import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime


class NewInstructorEvent(SimulationEvent):
    @staticmethod
    def run(session: Session, day: datetime):
        if len(session.query(Instruktor).all()) < MAX_AMOUNT_OF_INSTRUCTORS:
            instructor = Instruktor.get_random(day)

            session.add(instructor)
