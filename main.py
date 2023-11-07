from events import SampleEvent
import random
import db
import random
from simulation_properties import DATE_FROM, DATE_TO, MAX_AMOUNT_OF_INSTRUCTORS, MAX_AMOUNT_OF_STUDENTS
from datetime import datetime, timedelta
from events import EventRegistry
from sqlalchemy.orm.session import Session

event_registry = EventRegistry()
event_registry.add_event(SampleEvent, 0.00)

def initial_fill(s: Session):
    AVG_PER_INSTRUCTOR = MAX_AMOUNT_OF_STUDENTS // MAX_AMOUNT_OF_INSTRUCTORS
    for i in range(MAX_AMOUNT_OF_INSTRUCTORS//2):
        instructor = db.Instruktor.get_random(DATE_FROM)
        s.add(instructor)


        for j in range(random.randint(0, AVG_PER_INSTRUCTOR)):
            student = db.Krusant.get_random(DATE_FROM)
            s.add(student)


            kurs = db.Kurs(data_rozpoczecia=DATE_FROM)
            kurs.ko_kursant_id = student.id
            kurs.ko_instruktor_id = instructor.id
            s.add(kurs)
    s.commit()

initial_fill(db.session)

kursy = db.session.query(db.Kurs).all()

SIMULATION_DAYS =  (DATE_TO - DATE_FROM).days

for day in range(SIMULATION_DAYS):
    current_day = DATE_FROM + timedelta(days=day)

    # run events for this day
    event_registry.fire_events(db.session, current_day)

    # run special events

    # terminarz uzupelnienie
    instructors = db.session.query(db.Instruktor).all()
    for instructor in instructors:
        free_hours = [0 for i in range(24)]
        # checks for instructor
        instructors_kursy = db.session.query(db.Kurs).filter(db.Kurs.ko_instruktor_id == instructor.id).all()
        # print(instructors_kursy)
        students = [db.session.query(db.Krusant).filter_by(id=kurs.ko_kursant_id).first() for kurs in instructors_kursy]

        # print(students)
        
        pass


db.session.close()