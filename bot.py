import discord
import json
from discord.ext import commands

import construire_info

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

id_inconnu = "Cet ID n'est associé à aucune carte."

@bot.command()
async def print(ctx, print):
    await ctx.send(print)

@bot.command()
async def description(ctx, id_carte):
    carte = construire_info.construire_carte(id_carte)
    await ctx.send(
       id_inconnu if carte == -1 else carte.miseEnFormeFR()
      )

@bot.command()
async def traduction(ctx, id_carte):
    carte = construire_info.construire_carte(id_carte, True)
    await ctx.send(
      id_inconnu if carte == -1 else carte.miseEnFormeFR()
      )

bot.run(TOKEN)