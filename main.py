import db
from db import *

ed_samochod = db.Samochod(marka="Saudi", rok_produkcji=2001, model="Arabia")
db.session.add(ed_samochod)

cars = db.session.query(db.Samochod).all()
for car in cars:
    print(car)

print(instruktor.random())

