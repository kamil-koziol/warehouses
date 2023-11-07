from .simulation_event import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime


class NewStudentEvent(SimulationEvent):
    @staticmethod
    def run(session: Session, day: datetime):
        # TODO
        print("ZRUP TO")
