from sqlalchemy.orm import Session

from db import *


def get_number_of_active_courses(session: Session):
    amount = 0
    for k in session.query(Kurs).all():
        if k.data_zakonczenia is not None:
            amount += 1
    return amount


def get_number_of_active_instructors(session: Session):
    amount = 0
    for k in session.query(Instruktor).all():
        if k.data_zwolnienia is not None:
            amount += 1
    return amount
