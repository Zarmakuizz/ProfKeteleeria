# indentify.py
import re

class Identify:

    # TODO return a Pokémon Card data for each match
    # TODO build Pokémon card data from various sources, lazy mode
    def cards(self, message): 
        matches = re.findall(r"\[([^[\]]+)\]", message)
        return matches[:4]