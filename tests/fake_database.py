# fake_database.py

from functools import reduce
import re
from typing import List
from src.card import Card
from src.databaseInterface import DatabaseInterface
from src.series import Series

class FakeDatabase(DatabaseInterface): 

    def __init__(self, cards: List[Card]):
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
