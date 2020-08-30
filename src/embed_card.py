# embed_card.py

import discord
from string import Template
from src.card import Card
from src.utilities_interface import UtilitiesInterface

class EmbedCard:
    border_colors = [''] * 17

    # TODO nice card details display 
    def __init__(self, card: Card, util: UtilitiesInterface):
        self.card = card
        self.utilities = util

    def get(self): 
        return self.__basic_embed()

    """ Simple embed that displays the card's image """
    def __basic_embed(self): 
        card = self.card
        embed = discord.Embed()
        embed.type = "rich"

        (r, g, b) = self.utilities.get_color(card.card_type)
        embed.colour = discord.Colour.from_rgb(r=r, g=g, b=b)
        link = self.utilities.get_link_to_thumbnail(card)
        embed.set_image(url=link)

        name = card.name
        icon = self.utilities.get_type_img(card.card_type)
        embed.set_author(name=name, icon_url=icon)

        return embed

    """ More powerful embed that displays the card's details instead """
    def __rich_embed(self):
        # FIXME Needs actual Card Details in a database in order to be useful
        card = self.card
        embed = discord.Embed()
        embed.type = "rich"

        (r, g, b) = self.utilities.get_color(card.card_type)
        embed.colour = discord.Colour.from_rgb(r=r, g=g, b=b)
        link = self.utilities.get_link_to_thumbnail(card)
        embed.set_thumbnail(url=link)

        name = card.name # TODO add HP to the title
        icon = self.utilities.get_type_img(card.card_type)
        embed.set_author(name=name, icon_url=icon)

        embed.description = card.series.name + " " + str(card.number) + "/" + str(card.series.total) # todo set official total

        # TODO field management
        # TODO ability icon if doable
        # TODO handle Pokémon Powers, Poké Powers, Poké Bodies, Ancient Traits also
        embed.add_field(name="Ability : Saucisse", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", inline=False)
        # TODO NRJ icons, GX icon if doable
        # NRJ: G F O E P C T M F D I , if it can't be iconized
        embed.add_field(name="[E][E][E] Full Blitz : 150", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", inline=False)
        embed.add_field(name="[E][E][E]+ Tag Bolt GX : 200", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ", inline=False)
        # TODO rule reminder generator
        # TODO Weakness/Resistance/Retreat cost generator
        embed.add_field(name="Si un Pokémon GX est mis KO, votre adversaire prend 2 récompenses", 
                        value="Faiblesse : [C] | Résistance : [M] | Coût de retraite : [I][I]", inline=False)

        # TODO footer with links
        return embed