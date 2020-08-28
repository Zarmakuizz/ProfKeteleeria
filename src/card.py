# card.py

from src.series import Series

class Card:

    # TODO load a read card data
    def __init__(self, name: str, series: Series): 
        self.name = name
        self.series = series

    def is_valid(self) -> bool: 
        return True
    
    def __eq__(self, other_card) -> bool:
        return self.name == other_card.name and self.is_valid() and other_card.is_valid()
    
    def __str__(self) -> str:
        return self.name + str(self.series)
    
    def __repr__(self) -> str:
        return str(self)