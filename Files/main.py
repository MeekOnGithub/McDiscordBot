import discord
from discord.ext import commands
from McDiscordBot.config import token, prefix, joinchannel
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
from javascript import require, On
from discord import Intents
import os
import time
import sys
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

intents = Intents.default()
intents.members = True


bot = commands.Bot(command_prefix = prefix, description = "Have a nice day ;D", intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
	os.system("cls")

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(joinchannel)
	embed=discord.Embed(title=f"{message.author.mention}, bienvenue sur le serveur" ,color=0xaf2323)
	await channel.send(embed=embed)
	print(f"{member.name}, a rejoin le serveur !")
	member = member.message.author
	role = get(member.server.roles, name="MEMBRE")
	await bot.add_roles(member, role)

@bot.event
async def on_member_leave(member):
	embed=discord.Embed(title=f"{message.author.mention}, est partie" ,color=0xaf2323)
	await channel.send(embed=embed)
	print(f"{member.name}, a quitté le serveur !")


@bot.command()
async def start(ctx):
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
	fait_choix = await ctx.send("Voulez vous démarrer le bot ? <:robott:977535335246491708>", components=[action_row])

	def check(m):
		return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

	button_ctx = await wait_for_component(bot, components=action_row, check=check)
	if button_ctx.custom_id == "oui":
		await fait_choix.delete()
		embed=discord.Embed(title="Préparation du bot <a:954143028740784189:977625478108156014>")
		embed.add_field(name=":warning: Cette operation peut prendre du temps :warning:", value="Bot...", inline=False)
		message = await ctx.send(embed=embed)
		print("Lancement du bot")
		os.system("python start.py")
	else:
		await fait_choix.delete()


		

bot.run(token)
