# indentify.py
import re

from typing import List
from src.card import Card
from src.error_card import ErrorCard
from src.databaseInterface import DatabaseInterface
from src.series import Series

class Search:

    def __init__(self, db: DatabaseInterface):
        self.database = db

    # TODO return a Pokémon Card data for each match
    # TODO build Pokémon card data from various sources, lazy mode
    def find_cards(self, message) -> List[Card]: 
        matches = re.findall(r"\[([^[\]]+)\]", message)
        result = list(map(self.card, matches[:4]))
        return result

    def card(self, card_raw_text: str) -> Card: 
        names, series, number = self.__identify_card(card_raw_text)

        candidates = self.__get_cards(names)
        if(series):
            candidates = self.__filter_by_series(candidates, series)
        if(number):
            candidates = self.__filter_by_number(candidates, int(number))
        
        candidates = self.__get_last_released(candidates)
        if(candidates):
            return candidates[0]
        else:
            return ErrorCard()
    
    
    def __identify_card(self, card_raw_text: str):
        names = card_raw_text.split(' ')
        series = None
        number = None
        while(len(names) > 1):
            current = names[-1]
            if(current.isnumeric()):
                number = names.pop(-1)
                continue
            if(self.database.is_series(current)):
                series = self.database.get_series(current)
                names.pop(-1)
                continue
            break
        # TODO filter bad strings
        return (names, series, number)
            
    
    def __get_cards(self, names: List[str]) -> List[Card]: 
        candidates = self.database.getCards(names)
        return candidates

    def __filter_by_series(self, cards: List[Card], series: Series) -> List[Card]:
        candidates = []
        for card in cards:
            if card.series == series:
                candidates.append(card)
        
        return candidates
    
    def __filter_by_number(self, cards: List[Card], number: int) -> List[Card]:
        candidates = []
        for card in cards:
            if card.number == number:
                candidates.append(card)
        return candidates
    
    def __get_last_released(self, cards: List[Card]) -> List[Card]:
        cards.sort(key= lambda card: card.series.date, reverse=True)
        return cards
    

    