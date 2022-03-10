import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="YOU PREFIXE")

@bot.event
async def on_ready():
    print("I'm alive")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run("YOUR TOKEN BOT")
