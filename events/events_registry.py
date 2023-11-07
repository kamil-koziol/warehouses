import random
from typing import List, NamedTuple
from events import SimulationEvent
from sqlalchemy.orm import Session
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

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

        def thread_worker(event: EventProbability):
            if random.random() < event.probability:
                event.event.run(session, day)

        with ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(thread_worker, self.events)