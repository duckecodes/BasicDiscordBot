# Imports

import discord
from discord.ext import commands
from colorama import Fore as C
import time
from random import choice

# Bot token goes under here

token = "putyourbottokenhere"

# Bot prefix for commands

bot = commands.Bot(command_prefix="ducke")
bot.remove_command("help")

# Makes the bot appear online


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name="Created by... duckecodes on github"))


# If the bot turns on without a error it will say what is below this message


@bot.event
async def on_connect():
    print(f""" 
{C.BLUE}Logged in as: {bot.user}{C.BLUE}
{C.BLUE}Prefix: ducke{C.BLUE}
""")


# Says pong back to you


@bot.command()
async def ping(ctx):
    await ctx.send("**pong!**")
    try:
        print(f"{C.GREEN}[+] Successfully sent message{C.GREEN}")
    except:
        print(f"{C.RED}[-] Unsuccessfully sent message{C.RED}")
        pass


# Says hi back to you


@bot.command()
async def hello(ctx):
    await ctx.send("Hi, hows your day been?")
    try:
        print(f"{C.GREEN}[+] Successfully sent message{C.GREEN}")
    except:
        print(f"{C.RED}[-] Unsuccessfully sent message{C.RED}")
        pass


# Scare people by doing the command under here (This is a fake command. This command wont hack the server!)


@bot.command()
async def hack(ctx):
    await ctx.send("Stealing info...")
    time.sleep(3)
    await ctx.send("Leaking everyones info...")
    time.sleep(3)
    await ctx.send("JK!!!!!!!!")
    try:
        print(f"{C.GREEN}[+] Successfully sent message{C.GREEN}")
    except:
        print(f"{C.RED}[-] Unsuccessfully sent message{C.RED}")
        pass


# Says who created the bot (Created by... duckecodes on github)


@bot.command()
async def dev(ducke):
    await ducke.send("Created by... duckecodes on github")
    try:
        print(f"{C.GREEN}[+] Successfully sent message{C.GREEN}")
    except:
        print(f"{C.RED}[-] Unsuccessfully sent message{C.RED}")
        pass


# Says whos the gayest server member


@bot.command()
async def gay(ctx):
    user = choice(ctx.message.channel.guild.members)
    await ctx.send(f"Gayest member: {user.mention}")
    try:
        print(f"{C.GREEN}[+] Successfully sent message{C.GREEN}")
    except:
        print(f"{C.RED}[-] Unsuccessfully sent message{C.RED}")
        pass


bot.run(token, bot=True)
