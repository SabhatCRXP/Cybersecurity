import sys
from Model.Person import Person
from CsvHelper import CsvHelper

def main_menu():
    csvHelper = CsvHelper()
    persons = csvHelper.readCsvFile("fake_people_data_cs_datetime.csv", Person)

    sorted_on_first_name = sorted(persons, key=lambda p: p.first_name)
    list(map(print, sorted_on_first_name))

    csvHelper.writeCsvFile("SortedList.csv", sorted_on_first_name)

main_menu()