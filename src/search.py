# indentify.py
import re

from src.card import Card
from src.error_card import ErrorCard
from src.databaseInterface import DatabaseInterface

class Search:

    def __init__(self, db: DatabaseInterface):
        self.database = db

    # TODO return a Pokémon Card data for each match
    # TODO build Pokémon card data from various sources, lazy mode
    def find_cards(self, message): 
        matches = re.findall(r"\[([^[\]]+)\]", message)
        result = list(map(self.card, matches[:4]))
        return result

    def card(self, card_name): 
        candidates = self.database.getCards(card_name)
        if(candidates):
            return candidates[0]
        else:
            return ErrorCard()