from nextcord import Intents
from nextcord.ext import commands, menus, tasks
from McDiscordclient.config import token, prefix, joinchannel
from javascript import require, On
import os
import time
import sys
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

intents = Intents.default()
intents.members = True


client = commands.client(command_prefix = prefix, description = "Have a nice day ;D", intents=intents)
slash = SlashCommand(client, sync_commands=True)



@client.event
async def on_ready():
	os.system("cls")


class botconnection(nextcord.ui.Modal):
	def __init__(self):
		super().__init__("Création de l'embed")  

	 
		self.title = nextcord.ui.TextInput(
			label="Pseudo du bot",
			min_length=2,
			max_length=50,
		)
		self.add_item(self.title)

	async def callback(self, interaction: nextcord.Interaction) -> None:
		try:
			if port == None:
				port == "25565"
			else:
				port == port
			host = ip
			port = port
			RANGE_GOAL = 1
			BOT_USERNAME = self.title
			bot.loadPlugin(pathfinder.pathfinder)
			print("En cours de connection...")
			await interaction.send(embed=embed, view=view)
		except Exception as e:
			print(boterror + " " + (str(e)))



class Start(nextcord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@nextcord.ui.button(label="Oui", style=nextcord.ButtonStyle.green)
	async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		await interaction.response.send_message("Connection en cours...", ephemeral=True)
		modal = botconnection()
		await interaction.response.send_modal(modal)
	
		self.value = True

		self.stop()

	@nextcord.ui.button(label="Non", style=nextcord.ButtonStyle.red)
	async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		await interaction.response.send_message("Annulation avec succés :smile:", ephemeral=True)
		pass
		self.value = False
		self.stop()

@client.slash_command(
	name="start",
	description="Permet démmarrer le client")
async def stop(interaction):
	try:
		view = Start()
		embed = nextcord.Embed(title="Êtes-vous sur de vouloir démarrer le client?")
		interaction = await interaction.send(embed=embed, view=view, ephemeral=True)
		await view.wait()


	except Exception:
		print("lol")

class Stop(nextcord.ui.View):
	def __init__(self):
		super().__init__()
		self.value = None

	@nextcord.ui.button(label="Oui", style=nextcord.ButtonStyle.green)
	async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		await interaction.response.send_message("Au revoir :slight_smile: :wave:", ephemeral=True)
		await sys.exit()
		self.value = True

		self.stop()


	@nextcord.ui.button(label="Non", style=nextcord.ButtonStyle.green)
	async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
		await interaction.response.send_message("Annulation avec succés :smile:", ephemeral=True)
		pass
		self.value = False
		self.stop()

@client.slash_command(
	name="stop",
	description="Permet de faire déconnecter le client")
async def stop(interaction):
	try:
		view = Stop()
		embed = nextcord.Embed(title="Vous êtes sûr de vouloir éteindre le client ?")
		interaction = await interaction.send(embed=embed, view=view, ephemeral=True)
		await view.wait()
	except Exception:
		print("lol")

@On(bot, 'spawn')
def handle(ctx, *args):
	print("Le bot a spawn !")



@On(bot, "end")
def handle(*args):
	print("Le bot est déconnecter", args)

client.run(token)
