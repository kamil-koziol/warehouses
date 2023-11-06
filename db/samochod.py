from sqlalchemy import Column, Integer, String, Date, Boolean
from db import Base
from utils import *
from simulation_properties import *

cars = read_from_file('data/samochody.csv')


class Samochod(Base):
    __tablename__ = 'samochod'

    id = Column(Integer, primary_key=True)
    marka = Column(String(20))
    rok_produkcji = Column(Integer)
    model = Column(String(30))

    @staticmethod
    def get_random():
        car = Samochod()
        rc = random.choice(cars)
        car.marka, car.model, car.rok_produkcji = rc["Marka"], rc["Model"], DATE_FROM.year - datetime.now().year + int(rc["Rok"])
        return car