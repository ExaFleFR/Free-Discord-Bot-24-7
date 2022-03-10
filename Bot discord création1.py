import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print("I'm alive")

@bot.command(hey)
async def ping(ctx):
    await ctx.send("pong")

bot.run("OTUxNDg0MTY3NTIxMjAyMjM4.YioIrw.-8SBhLHx1GGiCp1pioUwcbfSCDg")