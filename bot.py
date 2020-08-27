# bot.py
import os

import discord
from identify import Identify
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
identifier = Identify()

client = discord.Client()

@client.event
async def on_ready():
    # Feedback to ensure the bot is on
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return # avoid recursion

    cards = identifier.cards(message.content)
    for card in cards: 
        # TODO display card details
        # TODO nice card details display 
        print(card) 
        await message.channel.send("TODO display cards for: " + card)


client.run(TOKEN)