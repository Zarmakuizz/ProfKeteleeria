# databaseInterface.py

from typing import List
from src.card import Card
from src.series import Series

class DatabaseInterface: 

    def getCards(self, name: List[str]) -> List[Card]:
        pass

    def is_series(self, abbreviation: str) ->bool:
        pass
    
    def get_series(self, abbreviation: str) -> Series:
        pass