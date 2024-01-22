import discord
import json
from discord.ext import commands

# Opens the file in read-only mode and assigns the contents to the variable cfg to be accessed further down
with open('config.json', 'r') as cfg:
  # Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
  data = json.load(cfg) 

TOKEN = data["token"]

description = '''Bot de description des cartes.

Traductions disponibles.
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!',description=description, intents=intents)

@bot.command()
async def print(ctx, print):
    await ctx.send(print)

bot.run(TOKEN)