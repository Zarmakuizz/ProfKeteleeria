# card.py

import discord
from src.series import Series

class Card:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.number = 0
        self.card_type = 0
        self.series = None

    @staticmethod
    def from_test_data(name: str, series: Series, number):
        card = Card()
        card.name = name 
        card.series = series
        card.number = number

        return card


    def is_valid(self) -> bool: 
        return True
    
    def get_embed(self, utilities): 
        from src.embed_card import EmbedCard # workaround against circular imports
        embed = EmbedCard(self, utilities).get()
        return embed
    
    def __eq__(self, other) -> bool:
        return (self.is_valid() and other.is_valid() 
                and self.name == other.name 
                and self.number == other.number)
    
    def __str__(self) -> str:
        return self.name + str(self.series)
    
    def __repr__(self) -> str:
        return str(self)