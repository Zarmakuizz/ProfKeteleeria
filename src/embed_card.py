# embed_card.py

import discord
from src.card import Card

class EmbedCard:
    embed = None;

    def __init__(self, card: Card):
        self.embed = discord.Embed()
        self.embed.type = "rich"
        self.embed.colour = discord.Colour.from_rgb(255, 255, 0) # TODO color based on card type

        self.embed.title = card.name 
        # TODO HP & Card type
        self.embed.description = card.series.name + " " + str(card.number) + "/" + "XXX" # todo set official total

        # TODO field management
        # TODO ability icon
        self.embed.add_field(name="Ability: Saucisse", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", inline=False)
        # TODO NRJ icons, GX icon
        self.embed.add_field(name="EEE Tag Bolt : 150", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", inline=False)

    def getEmbed(self):
        return self.embed