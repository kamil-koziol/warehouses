import random
import uuid
from uuid import uuid4

from sqlalchemy import Column, Integer, String, Date, Boolean, Uuid
from db import Base
from simulation_properties import *
from utils import *


class Krusant(Base):
    __tablename__ = 'krusant'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    imie = Column(String(20))
    nazwisko = Column(String(30))
    pesel = Column(String(11))
    data_urodzenia = Column(Date)
    plec = Column(Boolean)

    @staticmethod
    def get_random(now: datetime):
        birth_date = get_rand_date_between_years(now.year - STUDENT_AGE_MAX, now.year - STUDENT_AGE_MIN)

        student = Krusant()
        is_male = random.choice([True, False])
        student.imie, student.nazwisko = get_rand_name(is_male)
        student.plec = is_male
        student.data_urodzenia = birth_date
        student.pesel = generate_pesel(birth_date)
        return student
