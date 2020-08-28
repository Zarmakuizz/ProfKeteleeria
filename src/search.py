# indentify.py
import re

from typing import List
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

    def card(self, card_raw): 
        matches = re.search(r"(?P<name>\S+)(?: (?P<series>\S+))?(?: (?P<number>\S+))?", card_raw)
        name = matches.group('name')
        series = matches.group('series')
        number = matches.group('number')

        candidates = self.__get_cards(name)
        if(series):
            candidates = self.__filter_by_series(candidates, series)
        else:
            candidates = self.__get_last_released(candidates)

        if(candidates):
            return candidates[0]
        else:
            return ErrorCard()
    
    def __get_cards(self, name: str): 
        candidates = self.database.getCards(name)
        return candidates
    
    def __filter_by_series(self, cards: List[Card], series) -> List[Card]:
        candidates = []
        for card in cards:
            if card.series.matches(series):
                candidates.append(card)
        
        return candidates
    
    def __get_last_released(self, cards: List[Card]) -> List[Card]:
        cards.sort(key= lambda card: card.series.date, reverse=True)
        return cards
    
    