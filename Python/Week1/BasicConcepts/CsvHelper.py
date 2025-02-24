import csv
import os
from typing import Type, List

downloads_path = os.path.join(os.getenv("USERPROFILE"), "Downloads")

class CsvHelper:
    def readCsvFile(self, file_name: str, model: Type, custom_path: str = None) -> List:
        path = custom_path if custom_path else downloads_path
        file_path = os.path.join(path, file_name)

        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=";")

                objects = []
                for row in reader:
                    obj = model(**row)
                    objects.append(obj)

                return objects
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return []
    

    def writeCsvFile(self, file_name: str, data_list: list, custom_path: str = None):
        path = custom_path if custom_path else downloads_path
        file_path = os.path.join(path, file_name)

        if not data_list:
            print("Error: No data to write.")
            return

        headers = list(data_list[0].__dict__.keys())

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")
            writer.writeheader()

            for obj in data_list:
                writer.writerow(obj.__dict__)
