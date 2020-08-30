
from src.card import Card

class UtilitiesInterface:


    @staticmethod
    def get_color(id_type: int):
        return (255, 255, 255)
    
    @staticmethod
    def get_type_img(id_type: int) -> str:
        return "https://assets.pokemon.com/static2/_ui/img/cards/energy-types.png"
    
    @staticmethod
    def get_link_to_thumbnail(card: Card) -> str:
        return "https://assets.pokemon.com/assets/cms2/img/cards/web/SWSH3/SWSH3_EN_2.png"

    @staticmethod
    def is_Pokemon(card: Card) -> bool:
        return True

    @staticmethod
    def get_link_to_series(card: Card) -> str:
        return "https://www.pokemon.com/uk/pokemon-tcg/pokemon-cards/?"