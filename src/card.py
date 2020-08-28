# card.py

import discord
from src.series import Series

class Card:

    # TODO load a read card data
    def __init__(self, name: str, series: Series, number: int): 
        self.name = name
        self.series = series
        self.number = number

    def is_valid(self) -> bool: 
        return True
    
    def get_embed(self): 
        embed = discord.Embed()
        embed.title = self.name
        embed.description = self.series.name + " " + str(self.number) + "/" + "XXX" # todo set official total
        embed.add_field(name="Ability: Saucisse", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", inline=True)
        embed.type = "rich"
        embed.colour = discord.Colour.from_rgb(255, 255, 0)

        return embed
    
    def __eq__(self, other) -> bool:
        return (self.is_valid() and other.is_valid() 
                and self.name == other.name 
                and self.number == other.number)
    
    def __str__(self) -> str:
        return self.name + str(self.series)
    
    def __repr__(self) -> str:
        return str(self)