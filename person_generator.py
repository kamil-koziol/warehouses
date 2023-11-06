import pandas as pd
import random

names_df = pd.read_csv('Osoby/imi')
surename_df = pd.read_csv('nazwiska.csv')

rand_name = random.choice(names_df['Imię'])
rand_surename = random.choice(surename_df['Nazwisko'])

print("imię:", rand_name)
print("nazwisko:", rand_name)
