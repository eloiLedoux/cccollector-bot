import discord
import json

import construire_info

# Opens the file in read-only mode and assigns the contents to the variable cfg to be accessed further down
with open('config.json', 'r') as cfg:
  # Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
  data = json.load(cfg) 

TOKEN = data["token"]

bot = discord.Bot()

id_inconnu = "``` Cet ID n'est associé à aucune carte. ```"

@bot.command(description="Répète un peu pour voir.")
async def print(ctx, print):
    await ctx.respond(print)

@bot.command(description="Description d'une carte à partir de son code.")
async def description(ctx, id_carte):
    carte = construire_info.construire_carte(id_carte)
    await ctx.respond(
       id_inconnu if carte == -1 else ("```" + carte.miseEnFormeFR() + "```")
      )

@bot.command(description="Traduction d'une carte à partir de son code.")
async def traduction(ctx, id_carte):
    carte = construire_info.construire_carte(id_carte, True)
    await ctx.respond(
      id_inconnu if carte == -1 else ("```" + carte.miseEnFormeFR() + "```")
      )

bot.run(TOKEN)