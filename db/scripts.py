from sqlalchemy.orm import Session

from db import *


def get_number_of_active_courses(session: Session):
    return session.query(Kurs).filter(Kurs.data_zakonczenia.isnot(None)).count()



def get_number_of_active_instructors(session: Session):
    return session.query(Instruktor).filter(Instruktor.data_zwolnienia.isnot(None)).count()
