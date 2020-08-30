# fake_database.py

from datetime import date
from functools import reduce
import re
from typing import List
from src.card import Card
from src.databaseInterface import DatabaseInterface
from src.series import Series

class FakeDatabase(DatabaseInterface): 

    def __init__(self):
        teamUp = Series.from_test_data("Team Up", date(2019, 2, 1), ["SM9", "TEU", "SM09"])
        rebelClash = Series.from_test_data("Rebel Clash", date(2020, 5, 1), ["SWSH2"])
        celestialStorm = Series.from_test_data("Celestial Storm", date(2018, 8, 1), ["SM7"])
        oldSet = Series.from_test_data("who cares", date(2015, 1, 1), [""])

        cards = [
            Card.from_test_data("Jirachi", oldSet, 42),
            Card.from_test_data("Pikachu", oldSet, 25),
            Card.from_test_data("Jirachi", teamUp, 99),
            Card.from_test_data("Jirachi {*}", celestialStorm, 80),
            Card.from_test_data("Pikachu GX", oldSet, 26),
            Card.from_test_data("Pikachu EX", oldSet, 27),
            Card.from_test_data("Pikachu&Zekrom GX", teamUp, 33),
            Card.from_test_data("Intelleon V", rebelClash, 49),
            Card.from_test_data("Intelleon Vmax", rebelClash, 50),
        ]
        self.cards = cards
        self.__build_series()

    def getCards(self, names: List[str]): 
        result = []
        safe_names = list(map(self.__sanitize_name, names))
        for card in self.cards:
            safe_card_name = card.name.lower()
            name_parts_matches = list(map(lambda name: name in safe_card_name, safe_names))
            is_matching = reduce(lambda a,b: a and b, name_parts_matches)
            if is_matching:
                result.append(card)

        return result
    
    def __sanitize_name(self, name: str) -> str:
        result = name.lower()
        result = re.sub(r"-ex$", " ex", result)
        result = re.sub(r"-gx$", " gx", result)
        result = re.sub(r"-v$", " v", result)
        result = re.sub(r"-vmax$", " vmax", result)
        return result

    def is_series(self, abbreviation: str) ->bool:
        return abbreviation in self.series
    
    def get_series(self, abbreviation: str) -> Series:
        return self.series[abbreviation]
    
    def __build_series(self): 
        self.series = {}
        for card in self.cards:
            for abbreviation in card.series.abbreviations:
                self.series[abbreviation] = card.series
