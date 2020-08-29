# embed_card.py

import discord
from src.card import Card

class EmbedCard:
    
    # TODO nice card details display 
    def __init__(self, card: Card):
        self.card = card

    # TODO break down per responsibility once it's properly implemented
    def getEmbed(self):
        card = self.card
        embed = discord.Embed()
        embed.type = "rich"
        embed.colour = discord.Colour.from_rgb(255, 255, 0) # TODO color based on card type
        embed.set_thumbnail(url="https://www.pokecardex.com/assets/images/sets/SWSH2/1.jpg") # TODO get URL based on actual card

        # TODO get actual card icon (nrj type or trainer type)
        name = card.name + " | 240 HP"
        embed.set_author(name=name, icon_url="https://www.pokecardex.com/forums/images/smilies/energy-types_10.png") 
        # TODO HP & Card type
        embed.description = card.series.name + " " + str(card.number) + "/" + "XXX" # todo set official total

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
        embed.add_field(name="Si un Pokémon GX est mis KO, votre adversaire prend 2 récompenses", value="Faiblesse : [C] | Résistance : [M] | Coût de retraite : [I][I]", inline=False)
        return embed