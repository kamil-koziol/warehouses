import random

from utils import read_from_file

instructor_index = 0
student_index = 0

m_names = read_from_file('data/imiona_meskie.csv')
m_surname = read_from_file('data/nazwiska_meskie.csv')
f_names = read_from_file('data/imiona_zenskie.csv')
f_surname = read_from_file('data/nazwiska_zenskie.csv')


def get_rand_name(male: bool):
    if male:
        return random.choice(m_names), random.choice(m_surname)
    else:
        return random.choice(f_names), random.choice(f_surname)
