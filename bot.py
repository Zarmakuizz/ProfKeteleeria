# bot.py
import os

import discord
from dotenv import load_dotenv
from src.search import Search
from tests.fake_database import FakeDatabase # Fake initialization - use a fake database to have your bot working
from src.utilities_interface import UtilitiesInterface # Fake initialization - you need to extend the Interface classes to fit your database


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# Fake initialization - use a fake database to have your bot working
db = FakeDatabase()
utilities = UtilitiesInterface
# / TEMP - you will need to extend the Interfaces in order to interact with your own database
searcher = Search(db, utilities)
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
        if card.is_valid():
            await message.channel.send(embed=card.get_embed(utilities))
        else:
            await message.add_reaction("\U0000274C") # X emoji


client.run(TOKEN)