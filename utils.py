import random
from datetime import datetime
import csv

def get_rand_date_between_years(from_year: int, to_year: int):
    year = random.randint(from_year, to_year)

    month = random.randint(1, 12)
    day = random.randint(1, 28)

    return datetime(year, month, day)


def generate_pesel(date_of_birth):
    # Extract the year, month, and day from the date_of_birth
    year = date_of_birth.year - 1900  # Subtract 1900 to get the year part
    # Extract the month, and add 80 for females
    month = date_of_birth.month
    if date_of_birth.month > 9:
        month += 80
    # Extract the day
    day = date_of_birth.day

    # Generate a random 4-digit identification number
    identification = random.randint(0, 9999)

    # Format the PESEL as: YYMMDDXXXX
    pesel = f'{year:02}{month:02}{day:02}{identification:04}'

    # Calculate the PESEL checksum digit
    checksum = calculate_pesel_checksum(pesel)

    # Add the checksum digit to the PESEL
    pesel += str(checksum)

    return pesel


def calculate_pesel_checksum(pesel):
    weights = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
    checksum = sum(int(p) * w for p, w in zip(pesel, weights)) % 10
    return (10 - checksum) % 10


def read_from_file(filepath: str):
    data = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data