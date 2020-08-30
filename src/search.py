# indentify.py
import re

from datetime import date
from typing import List
from src.card import Card
from src.error_card import ErrorCard
from src.databaseInterface import DatabaseInterface
from src.series import Series
from src.utilities_interface import UtilitiesInterface

class Search:

    def __init__(self, db: DatabaseInterface, util:UtilitiesInterface) :
        self.database = db
        self.utilities = util

    def find_cards(self, message) -> List[Card]: 
        matches = re.findall(r"\[([^[\]]+)\]", message)
        result = list(map(self.card, matches[:4]))
        return result

    def card(self, card_raw_text: str) -> Card: 
        names, series, number = self.__identify_card(card_raw_text)

        candidates = self.__get_cards(names)
        if(series and self.__is_list_valid(candidates)):
            candidates = self.__filter_by_series(candidates, series)
        if(number and self.__is_list_valid(candidates)):
            candidates = self.__filter_by_number(candidates, int(number))
        
        if(self.__is_list_valid(candidates)):
            candidates = self.__remove_long_names(candidates)
            candidates = self.__get_last_released(candidates)
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
            # Expedition had the "EX" abbreviation - clashes with ex cards
            if(current != "EX" and self.database.is_series(current)):
                series = self.database.get_series(current)
                names.pop(-1)
                continue
            break
        # TODO filter bad strings
        return (names, series, number)
            
    
    def __get_cards(self, names: List[str]) -> List[Card]: 
        candidates = self.database.getCards(names)
        return candidates

    def __is_list_valid(self, list)-> bool:
        return list and ErrorCard() not in list

    def __filter_by_series(self, cards: List[Card], series: Series) -> List[Card]:
        candidates = []
        for card in cards:
            if card.series == series:
                candidates.append(card)
        
        return candidates
    
    def __filter_by_number(self, cards: List[Card], number: int) -> List[Card]:
        candidates = []
        for card in cards:
            if int(card.number) == number: # ensure same type
                candidates.append(card)
        return candidates
    
    def __remove_long_names(self, cards: List[Card]) -> List[Card]: 
        # Do not filter on trainer/NRJ cards - 
        are_trainers = True 
        for card in cards:
            if self.utilities.is_Pokemon(card):
                are_trainers = False
                break
        if(are_trainers):
            return cards

        cards.sort(key= lambda card: len(card.name))
        shortest_length = len(cards[0].name)
        result = list(filter(lambda card: len(card.name) <= shortest_length, cards))
        return result
    
    def __get_last_released(self, cards: List[Card]) -> List[Card]:
        tooOld = date(1990, 1, 1)
        cards.sort(key= lambda card: card.series.date or tooOld, reverse=True)
        return cards
    

    