import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix= "hot ",case_insensitive=True)
apikey = open("secret.key").read()

@client.command()
async def start(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    
@client.command()
async def stop(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def restart(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Hot bot ready")

for fileName in os.listdir("./cogs"):
    if fileName.endswith(".py"):
        client.load_extension(f"cogs.{fileName[:-3]}")
        
client.run(apikey)
