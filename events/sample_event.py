from .simulation_event import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime
import db

class SampleEvent(SimulationEvent):
    @staticmethod
    def run(session: Session, day: datetime):
        print(day, "Sample event run")
        print(session.query(db.Instruktor).all())