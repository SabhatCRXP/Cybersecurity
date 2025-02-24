from dataclasses import dataclass
from datetime import datetime

@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: datetime
    gender: str

    def __str__(self):
        return f"{self.first_name} {self.last_name} Born on {self.birth_date}, Gender: {self.gender}"
