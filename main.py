from db.kurs import print_csv
from events import SampleEvent
import db
import random
from simulation_properties import DATE_FROM, DATE_TO, MAX_AMOUNT_OF_INSTRUCTORS, MAX_AMOUNT_OF_STUDENTS, DEBUG_MODE
from datetime import datetime, timedelta
from events import *
from sqlalchemy.orm.session import Session
import time

event_registry = EventRegistry()
event_registry.add_event(SampleEvent, 0.00)
event_registry.add_event(FiredEvent, 1.0 / 150.0)
event_registry.add_event(NewStudentEvent, 0.3)
event_registry.add_event(NewInstructorEvent, 1.0 / 30.0)


def initial_fill(s: Session):
    for _ in range(MAX_AMOUNT_OF_INSTRUCTORS):
        car = db.Samochod.get_random()
        s.add(car)

    AVG_PER_INSTRUCTOR = MAX_AMOUNT_OF_STUDENTS // MAX_AMOUNT_OF_INSTRUCTORS
    for i in range(MAX_AMOUNT_OF_INSTRUCTORS // 2):
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

full_simulation_time = 0.0

for day in range(SIMULATION_DAYS):
    t1_start = time.perf_counter()
    current_day = DATE_FROM + timedelta(days=day)

    # run events for this day
    event_registry.fire_events(db.session, current_day)

    # run special events

    # terminarz uzupelnienie
    instructors = db.session.query(db.Instruktor).all()

    # todo: multithreaded instructors

    for instructor in instructors:
        # checks for instructor

        instructors_kursy = db.session.query(db.Kurs).filter(db.Kurs.ko_instruktor_id == instructor.id and db.Kurs.data_zakonczenia is not None).all()
        random.shuffle(instructors_kursy)

        terminarz = []

        remaining_hours = random.randint(6, 8)
        for kurs in instructors_kursy:
            # check if student can drive now

            # drive hours
            drive_hours = random.choices([1, 2, 3, 4], [1, 4, 2, 1])[0]

            if (remaining_hours < drive_hours):
                drive_hours = remaining_hours

            if (kurs.hours_remaining < drive_hours):
                drive_hours = kurs.hours_remaining

            remaining_hours -= drive_hours
            kurs.hours_remaining -= drive_hours

            if kurs.hours_remaining == 0:
                kurs.finish_course(db.session, current_day)
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

    if DEBUG_MODE: print(day)
    db.session.commit()
    t2_end = time.perf_counter()
    print(f"Day {day:04}, time: {t2_end - t1_start:0.4f} ms")
    full_simulation_time += t2_end - t1_start

print(f"Full simulation time: {full_simulation_time:0.4f} ms")
print_csv("WORD.csv")

db.session.close()
