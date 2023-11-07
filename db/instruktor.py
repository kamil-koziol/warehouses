import uuid

from sqlalchemy import Column, Integer, String, Date, Boolean, Uuid

from db import Base
from utils import *
from simulation_properties import *
from dataclasses import dataclass

@dataclass
class Instruktor(Base):
    __tablename__ = 'instruktor'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    imie = Column(String(20))
    nazwisko = Column(String(30))
    pesel = Column(String(11))
    poczatek_pracy = Column(Integer)
    data_urodzenia = Column(Date)
    data_zatrudnienia = Column(Date)
    data_zwolnienia = Column(Date, nullable=True)
    plec = Column(Boolean)

    number_of_active_courses = 0

    @staticmethod
    def get_random(now):
        birth_date = get_rand_date_between_years(DATE_FROM.year - INSTRUCTOR_AGE_MAX, DATE_FROM.year - INSTRUCTOR_AGE_MIN)

        ins = Instruktor()
        is_male = random.choice([True, False])
        rand_name = get_rand_name(is_male)
        ins.imie = rand_name[0]
        ins.nazwisko = rand_name[1]
        ins.plec = is_male
        ins.data_urodzenia = birth_date
        ins.poczatek_pracy = random.randint(birth_date.year + INSTRUCTOR_YEARS_EXPERIENCE_MAX, DATE_FROM.year)
        ins.data_zatrudnienia = now
        ins.pesel = generate_pesel(birth_date)
        return ins
