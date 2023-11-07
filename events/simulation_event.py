from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from datetime import datetime

class SimulationEvent(ABC):
    @staticmethod
    @abstractmethod
    def run(session: Session, day: datetime):
        pass
