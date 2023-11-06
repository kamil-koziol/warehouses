from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class SimulationEvent(ABC):
    @staticmethod
    @abstractmethod
    def run(session: Session, day: int):
        pass
