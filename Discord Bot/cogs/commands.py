import discord
import random
import os
import json
from discord.ext import commands

class Cmds(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Hot Bot is up and running")

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        if message.content == "hej":
            await message.channel.send(f"Hej <@{message.author.id}>")

    @commands.command()
    async def TierList(self,ctx):
        await ctx.send("https://tiermaker.com/create/thots-tierlist-940004")

    @commands.command()
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)  

    @commands.command()
    async def List(self, ctx):
        with open("./assets/text.json","r") as f:
            text=json.load(f)
        await ctx.send(", \n".join(list(text.values())))

    @commands.command()
    async def pick(self, ctx, name="Madison"):
        if f"{name.capitalize()}.png" in os.listdir("./thots"):
            file=discord.File(f"./thots/{name.capitalize()}.png")
            await ctx.channel.send(file=file)
        else:
            await ctx.send("Thot hittades inte!")

    @commands.command()
    async def thot(self, ctx):
        if ctx.author.bot:
            return

        thot=random.choice(os.listdir("./thots"))
        with open("./assets/text.json","r") as f:
            text=json.load(f)
            try:
                temp=text[thot]
            except:
                text[thot] = thot[:-4]
                with open("./assets/text.json","w") as v:
                    json.dump(text,v, sort_keys=True, indent=4)
            else:
                pass        
      
        file=discord.File(f"./thots/{thot}")
        await ctx.channel.send(content=text[thot],file=file)
        
    @commands.command()
    async def Tier(self, ctx):
        file=discord.File("./assets/Tier.png")
        await ctx.channel.send(file=file)
    
def setup(client):
    client.add_cog(Cmds(client))