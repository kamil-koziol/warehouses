import random

from sqlalchemy import Column, Integer, String, Date, Boolean

import utils
from db import Base
from person_generator import get_rand_name
from utils import *
from simulation_properties import *
from dataclasses import dataclass

@dataclass
class Instruktor(Base):
    __tablename__ = 'instruktor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    imie = Column(String(20))
    nazwisko = Column(String(30))
    pesel = Column(String(11))
    poczatek_pracy = Column(Integer)
    data_urodzenia = Column(Date)
    data_zatrudnienia = Column(Date)
    data_zwolnienia = Column(Date, nullable=True)
    plec = Column(Boolean)

    is_finishing_work = False

    @staticmethod
    def get_random(now):
        birth_date = get_rand_date_between_years(DATE_FROM.year - 40, DATE_FROM.year - 22)

        ins = Instruktor()
        is_male = random.choice([True, False])
        rand_name = get_rand_name(is_male)
        ins.imie = rand_name[0]["Imie"]
        ins.nazwisko = rand_name[1]["Nazwisko"]
        ins.plec = is_male
        ins.data_urodzenia = birth_date
        ins.poczatek_pracy = random.randint(birth_date.year + 22, DATE_FROM.year)
        ins.data_zatrudnienia = now
        ins.pesel = generate_pesel(birth_date)
        return ins
