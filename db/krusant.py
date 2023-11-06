import random

from sqlalchemy import Column, Integer, String, Date, Boolean
from db import Base
from person_generator import get_rand_name
from simulation_properties import *
from utils import *


class Krusant(Base):
    __tablename__ = 'krusant'

    id = Column(Integer, primary_key=True)
    imie = Column(String(20))
    nazwisko = Column(String(30))
    pesel = Column(String(11))
    data_urodzenia = Column(Date)
    plec = Column(Boolean)

    @staticmethod
    def get_random():
        birth_date = get_rand_date_between_years(DATE_FROM.year - 30, DATE_FROM.year - 18)

        student = Krusant()
        is_male = random.choice([True, False])
        student.imie, student.nazwisko = get_rand_name(is_male)
        student.plec = is_male
        student.data_urodzenia = birth_date
        student.pesel = generate_pesel(birth_date)
        return student
