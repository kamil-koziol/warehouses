import csv
import random
import uuid
from datetime import datetime, timedelta
from typing import List

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Uuid
from sqlalchemy.orm import Session

import simulation_properties
from db import Base, Instruktor, Krusant
from dataclasses import dataclass


class ExamTake:
    def __init__(self):
        self.pesel = ""  # Use str for strings
        self.id = 0  # Use int for integers
        self.time = datetime.now()
        self.result = False  # Use bool for boolean values


all_exams: List[ExamTake] = []


def decision(probability):
    return random.random() < probability


def print_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['pesel', 'id', 'time', 'result'])
        for exam in all_exams:
            writer.writerow([exam.pesel, exam.id, exam.time, exam.result])


def simulate_exam(day: datetime, c: Krusant):
    e = ExamTake()
    e.id = 0
    e.time = day
    e.pesel = c.pesel

    while not e.result:
        n_e = ExamTake()
        n_e.time = e.time + timedelta(days=random.randint(1, 5))
        n_e.pesel = c.pesel
        n_e.result = decision(0.4)
        all_exams.append(n_e)
        n_e.id = e.id + 1
        e = n_e


@dataclass
class Kurs(Base):
    __tablename__ = 'kurs'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    ko_kursant_id = Column(Uuid, ForeignKey('krusant.id'))
    ko_instruktor_id = Column(Uuid, ForeignKey('instruktor.id'))
    data_rozpoczecia = Column(Date)
    data_zakonczenia = Column(Date, nullable=True)
    hours_remaining = Column(Integer, default=simulation_properties.HOURS_IN_COURSE)

    def finish_course(self, session:Session, day):
        self.data_zakonczenia = day
        ins = session.query(Instruktor).get(self.ko_instruktor_id)
        ins.number_of_active_courses -= 1
        c = session.query(Krusant).get(self.ko_kursant_id)

        if simulation_properties.DEBUG_MODE:
            print(c.to_string() + " zakończył kurs")

        simulate_exam(day, c)
