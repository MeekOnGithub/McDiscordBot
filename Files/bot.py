
import discord
from McDiscordBot.config import token, usernamebot, prefix, joinchannel
from discord.ext import commands
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
import sys
from javascript import require, On
import os
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')


client = commands.Bot(command_prefix = prefix, description = "Have a nice day ;D")
slash = SlashCommand(client, sync_commands=True)
host = ip
port = port
RANGE_GOAL = 1
BOT_USERNAME = pseudo

bot = mineflayer.createBot({
  'host': host,
  'port': port,
  'username': BOT_USERNAME
})

bot.loadPlugin(pathfinder.pathfinder)
print("Loading /")

print("Lancement...")
if port == None:
  port == "25565"

@client.event
async def on_ready():
  os.system("cls")
  print("Ready !")

@On(bot, 'spawn')
def handle(ctx, *args):
  print("Le bot a spawn !")



@On(bot, "end")
def handle(*args):
  print("Bot ended!", args)

@client.command()
async def stop(ctx):
  buttons = [
    create_button(
      style=ButtonStyle.blue,
      label="Confirmer 🟢",
      custom_id="oui"
    ),
    create_button(
      style=ButtonStyle.danger,
      label="Annulez 🔴",
      custom_id="non"
    )
  ]
  action_row = create_actionrow(*buttons)
  fait_choix = await ctx.send("Vous êtes sûr de vouloir éteindre le bot ?", components=[action_row])

  def check(m):
    return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

  button_ctx = await wait_for_component(bot, components=action_row, check=check)
  if button_ctx.custom_id == "oui":
    await fait_choix.delete()
    print("Bot éteint...")
    sys.exit()
    message = await ctx.send("Bot éteint !")

  else:
    await fait_choix.delete()

client.run(token)




