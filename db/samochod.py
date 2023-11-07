import uuid

from sqlalchemy import Column, Integer, String,Uuid
from db import Base
from utils import *
from simulation_properties import *

cars = read_from_file('data/samochody.csv')

from dataclasses import dataclass

@dataclass
class Samochod(Base):
    __tablename__ = 'samochod'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    marka = Column(String(20))
    rok_produkcji = Column(Integer)
    model = Column(String(30))

    @staticmethod
    def get_random():
        car = Samochod()
        rc = random.choice(cars)
        car.marka, car.model, car.rok_produkcji = rc["Marka"], rc["Model"], DATE_FROM.year - datetime.now().year + int(rc["Rok"])
        car.id = uuid.uuid4()
        return car