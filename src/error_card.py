# error_card.py

from src.card import Card

class ErrorCard(Card):

    def __init__(self):
        super().__init__("", None, -1)
    
    def is_valid(self) -> bool:
        return False
    
    def __str__(self) -> str:
        return "Invalid Card"
    
    def __repr__(self) -> str:
        return str(self)
