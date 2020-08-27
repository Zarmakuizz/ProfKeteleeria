# indentify.py
import re

from src.card import Card

class Search:

    # TODO return a Pokémon Card data for each match
    # TODO build Pokémon card data from various sources, lazy mode
    def find_cards(self, message): 
        matches = re.findall(r"\[([^[\]]+)\]", message)
        result = list(map(self.card, matches[:4]))
        return result

    def card(self, card_name): 
        card = Card(card_name)
        return card