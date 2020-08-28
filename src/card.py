# card.py

from src.series import Series

class Card:

    # TODO load a read card data
    def __init__(self, name: str, series: Series, number: int): 
        self.name = name
        self.series = series
        self.number = number

    def is_valid(self) -> bool: 
        return True
    
    def __eq__(self, other) -> bool:
        return (self.is_valid() and other.is_valid() 
                and self.name == other.name 
                and self.number == other.number)
    
    def __str__(self) -> str:
        return self.name + str(self.series)
    
    def __repr__(self) -> str:
        return str(self)