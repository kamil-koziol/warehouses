from _datetime import datetime
from simulation_properties import DATE_FROM, DATE_TO, AMOUNT_OF_INSTRUCTORS, AMOUNT_OF_CARS, AMOUNT_OF_STUDENTS
from events import SampleEvent
import random
import db


SIMULATION_DAYS =  (DATE_TO - DATE_FROM).days

events = [(SampleEvent, 0.05)]
for day in range(SIMULATION_DAYS):
    # run events for this day
    for event in events:
        if random.random() < event[1]:
            event[0].run(db.session, day)

    # run special events

    # terminarz uzupelnienie


car = db.Samochod.get_random()
print(car)