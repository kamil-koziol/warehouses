import random
from typing import List, NamedTuple
from events import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime
import time
from simulation_properties import PERF


class EventProbability(NamedTuple):
    event: SimulationEvent
    probability: float


class EventRegistry:
    events: List[EventProbability]

    def __init__(self) -> None:
        self.events = []

    def add_event(self, event: SimulationEvent, probability: float):
        self.events.append(EventProbability(event, probability))

    def fire_events(self, session: Session, day: datetime):
        for event in self.events:
            if random.random() < event.probability:
                t1 = time.perf_counter()
                event.event.run(session, day)

                t2 = time.perf_counter()
                if PERF:
                    print("Event: " + event.event.__name__ + " took: " + str(t2 - t1) + " seconds")

