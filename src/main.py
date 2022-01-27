import random
import discord
from discord.ext import commands
import asyncio


my_token = ""
description = ''' An simple bot to show it works'''

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.command()
async def add(ctx, left: int, right:int):
    """Send message the sum of two number """
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice:str):
    """Rolls a dice"""
    try:
        rolls, limit = map(int,dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repeating..'):
    """Repeats a message"""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member:discord.Member):
    """Says when a member joined!"""
    await ctx.send(f'{member.name} joined in {member.joined_at}')

@bot.group()
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run(my_token)