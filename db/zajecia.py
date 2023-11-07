import uuid

from sqlalchemy import Column, Boolean, ForeignKey, DateTime, Uuid
from db import Base
from dataclasses import dataclass

@dataclass
class Zajecia(Base):
    __tablename__ = 'zajecia'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    ko_kurs_id = Column(Uuid, ForeignKey('kurs.id'))
    ko_samochod_id = Column(Uuid, ForeignKey('samochod.id'))
    poczatek = Column(DateTime)
    koniec = Column(DateTime)
    sie_odbyly = Column(Boolean)
