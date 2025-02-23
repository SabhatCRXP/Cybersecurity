import datetime

def calculate_age(birth_year):
    current_year = datetime.date.today().year
    return current_year - birth_year