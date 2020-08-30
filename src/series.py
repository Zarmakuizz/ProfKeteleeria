
from typing import List
from datetime import date

class Series: 

    def __init__(self):
        self.id = 0
        self.bloc = 0
        self.name = ""
        self.date = None
        self.total = 0
        self.abbreviations = []

    @staticmethod
    def from_test_data(name: str, date: date, abbreviations: List[str]):
        series = Series()
        series.name = name
        series.date = date
        series.abbreviations = abbreviations

        return series

    def add_abbreviation(self, abbreviation: str): 
        self.abbreviations.append(abbreviation)
    
    def matches(self, abbreviation: str) -> bool: 
        return abbreviation in self.abbreviations
    
    def __eq__(self, other):
        return (other != None 
            and self.name == other.name 
            and self.date == other.date)

    def __str__(self):
        return "[" + self.name + "|" + ','.join(self.abbreviations) + "]"

    def __repr__(self):
        return str(self)