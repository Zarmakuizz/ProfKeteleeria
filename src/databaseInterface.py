# databaseInterface.py

from typing import List
from src.card import Card

class DatabaseInterface: 

    def getCards(self, name: str) -> List[Card]:
        pass