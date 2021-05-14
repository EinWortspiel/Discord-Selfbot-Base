class Selfbot_base():
    Dev = "EinWortspiel 3#9998" #If you need help with anything just add this Discord Account - If you get an Error that this Account doesnt exist anymore try it with EinWortspiel 4#9998 
    Github = "EinWortspiel"

import discord
import asyncio
import colorama
import json

from colorama import Style, Fore, init
from discord.ext import commands, tasks
init()

with open("config.json") as f:
    config = json.load(f)

token = config.get("Token")
prefix = config.get("Prefix")

intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, intents = intents, self_bot = True)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{Fore.CYAN} {Style.BRIGHT}""""
    
    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗    ██████╗  █████╗ ███████╗███████╗
    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝
    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║       ██████╔╝███████║███████╗█████╗  
    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║       ██╔══██╗██╔══██║╚════██║██╔══╝  
    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║       ██████╔╝██║  ██║███████║███████╗
    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝       ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                              """)
    print(f"{Fore.CYAN} Base made by  {Selfbot_base.Dev}")
    print(f"{Fore.CYAN} Logged in as  {client.user.name}#{client.user.discriminator}")
    print(f"{Fore.CYAN} Use if you want c:\n")

@client.event
async def on_command(ctx):
    print(f"{Fore.CYAN}{Style.BRIGHT} Command used - {ctx.command.name}")

@client.command()
async def test(ctx):
    await ctx.message.delete()
    await ctx.send("Base by " + Selfbot_base.Dev)

client.run(token, bot = False)