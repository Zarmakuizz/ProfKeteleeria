# fake_database.py

from typing import List
from src.card import Card
from src.databaseInterface import DatabaseInterface

class FakeDatabase(DatabaseInterface): 

    def __init__(self, cards: List[Card]):
        self.cards = cards

    def getCards(self, name): 
        result = []
        for card in self.cards:
            if name in card.name:
                result.append(card)
        
        return result