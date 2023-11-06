from .simulation_event import SimulationEvent
from sqlalchemy.orm import Session

class SampleEvent(SimulationEvent):
    @staticmethod
    def run(session: Session, day: int):
        print(day, "Sample event run")