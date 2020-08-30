# ProfKeteleeria

Discord bot to retrieve and identify Pokémon cards

## Purpose

When a user types a [card name] in a Discord channel, this bot displays a card matching the request. Inspired by the Discord bot Millenium Eye, or [Bastion Bot](https://github.com/AlphaKretin/bastion-bot) that works in a similar fashion.

- Supports card search in English only
- Supports search with a card's abbreviation: [card name SET] (a set may have multiple abbreviations)
- Supports search with a card's number: [card name NUMBER]
- Or both: [card name SET NUMBER]
- In case of doubt, returns the most recent card, since it's often the only playable one, and players care mostly about cards in Standard format
- Aimed to support most card types, which also means that [Pikachu GX] returns Pikachu GX and not Pikachu&Zekrom GX

Disclaimer: the database used in this code base is a fake database with data defined by hand. 
If you want to use your own database, you should inherit both classes named "Interface" and provide your own implementation. Then modify bot.py (and .env) accordingly. I would recommend duplicating the battery of unit tests, using your own database implementation, to ensure that your implementation is valid.

## Setup

- Create a Discord Bot. [Full Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python)
- Install Python 3
- Using __pip__ (or __pip3__), install the following:
  - discord.py
  - python-dotenv
  - optional: pylint (for Visual Studio Code)
- Duplicate .env-template and rename it .env
- Modify the values in .env accordingly

Run the script run.sh to start the bot, unittest.sh to run the rests.

Follow the instructions in the [Python Discord Bot Full Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python)
 on how to declare your bot on Discord, and add it to your server.

## Dependencies

This project needs Python in version 3.5.3 at the very least. This is the minimum version supported by discord.py.

## License

See LICENSE file
