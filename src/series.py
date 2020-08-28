
from typing import List
from datetime import date

class Series: 
    abbreviations: List[str] = []

    def __init__(self, name: str, date: date, abbreviations):
        self.name = name
        self.date = date
        self.abbreviations = abbreviations

    def add_abbreviation(self, abbreviation: str): 
        self.abbreviations.append(abbreviation)
    
    def matches(self, abbreviation: str) -> bool: 
        return abbreviation in self.abbreviations
    
    def __eq__(self, other):
        return self.name == other.name and self.date == other.date

    def __str__(self):
        return "[" + self.name + "|" + ','.join(self.abbreviations) + "]"

    def __repr__(self):
        return str(self)