# error_card.py

from src.card import Card

class ErrorCard(Card):

    def __init__(self):
        super().__init__("")
    
    def is_valid(self) -> bool:
        return False
    
