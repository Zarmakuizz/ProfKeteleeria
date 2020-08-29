# bot.py
import os

import discord
from datetime import date # Temp
from src.card import Card # Temp
from src.search import Search
from src.series import Series # Temp
from dotenv import load_dotenv
from tests.fake_database import FakeDatabase # Temp


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# TEMP initialization
teamUp = Series("Team Up", date(2019, 2, 1), ["SM9", "TEU", "SM09"])
swordShield = Series("Sword&Shield", date(2020, 2, 1), ["SWSH1", "SSH", "EB1"])
rebelClash = Series("Rebel Clash", date(2020, 5, 1), ["SWSH2", "S2", "EB2"])
celestialStorm = Series("Celestial Storm", date(2018, 8, 1), ["SM7", "CES", "SM07"])
cards = [
        Card("Jirachi", teamUp, 99),
        Card("Jirachi {*}", celestialStorm, 80),
        Card("Pikachu", swordShield, 65),
        Card("Pikachu&Zekrom GX", teamUp, 33),
        Card("Intelleon V", rebelClash, 49),
        Card("Intelleon Vmax", rebelClash, 50),
]
db = FakeDatabase(cards)
# / TEMP
searcher = Search(db)
client = discord.Client()

@client.event
async def on_ready():
    # Feedback to ensure the bot is on
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return # avoid recursion

    cards = searcher.find_cards(message.content)
    for card in cards: 
        # TODO nice card details display 
        if card.is_valid():
            await message.channel.send(embed=card.get_embed())
        else:
            await message.add_reaction("\U0000274C") # X emoji


client.run(TOKEN)