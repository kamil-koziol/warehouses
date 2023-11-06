from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .model import Base
from .instruktor import Instruktor
from .krusant import Krusant
from .kurs import Kurs
from .samochod import Samochod
from .zajecia import Zajecia

engine = create_engine("sqlite:///db.sqlite", echo=False)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)  # once engine is available

session = Session()

Base.metadata.create_all(engine)
