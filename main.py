from events import SampleEvent
import db
import random
from simulation_properties import DATE_FROM, DATE_TO, MAX_AMOUNT_OF_INSTRUCTORS, MAX_AMOUNT_OF_STUDENTS
from datetime import datetime, timedelta
from events import EventRegistry
from sqlalchemy.orm.session import Session

event_registry = EventRegistry()
event_registry.add_event(SampleEvent, 0.00)

def initial_fill(s: Session):
    for _ in range(MAX_AMOUNT_OF_INSTRUCTORS):
        car = db.Samochod.get_random()
        s.add(car)

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
            instructor.number_of_active_courses += 1
            s.add(kurs)
    s.commit()

initial_fill(db.session)

SIMULATION_DAYS =  (DATE_TO - DATE_FROM).days

for day in range(SIMULATION_DAYS):
    current_day = DATE_FROM + timedelta(days=day)

    # run events for this day
    event_registry.fire_events(db.session, current_day)

    # run special events

    # terminarz uzupelnienie
    instructors = db.session.query(db.Instruktor).all()

    # todo: multithreaded instructors

    for instructor in instructors:
        # checks for instructor
        instructors_kursy = db.session.query(db.Kurs).filter(db.Kurs.ko_instruktor_id == instructor.id).all()
        random.shuffle(instructors_kursy)

        terminarz = []

        remaining_hours = 8
        for kurs in instructors_kursy:
            # check if student can drive now

            # drive hours
            drive_hours = random.choices([1,2,3, 4], [1,4,2, 1])[0]

            if(remaining_hours < drive_hours):
                drive_hours = remaining_hours

            if(kurs.hours_remaining < drive_hours):
                drive_hours = kurs.hours_remaining

            remaining_hours -= drive_hours
            kurs.hours_remaining -= drive_hours

            if kurs.hours_remaining == 0:
                # ended kurs
                pass

            
            terminarz.append((kurs, drive_hours))

            if remaining_hours == 0:
                break


        # generate zajecia from terminarz
        # todo: co jesli nie 8 godzin? sie nie odbyly

        staring_hour = random.randint(8, 14)
        current_time = current_day + timedelta(hours=staring_hour)

        for kurs, drive_hours in terminarz:
            zajecia = db.Zajecia()
            zajecia.poczatek = current_time
            zajecia.ko_kurs_id = kurs.id
            zajecia.ilosc_godzin = drive_hours
            zajecia.sie_odbyly = True
            zajecia.koniec = current_time + timedelta(hours=drive_hours)
            current_time += timedelta(hours=drive_hours)
            db.session.add(zajecia)

    print(day)
    db.session.commit()

db.session.close()