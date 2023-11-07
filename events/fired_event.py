import random

from db import Instruktor
from .simulation_event import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime
import db


class FiredEvent(SimulationEvent):
    @staticmethod
    def run(session: Session, day: datetime):
        ins: Instruktor = random.choice(session.query(db.Instruktor).all())
        ins.data_zwolnienia = day
