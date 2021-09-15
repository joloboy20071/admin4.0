import discord
from discord.ext import commands
import sys
import time

bot = commands.Bot(command_prefix='//',)

exec(open("commands.py").read())



token = "MzM3NjA1MzQyMjAyNjkxNjA1.YMN_gg.PqW_onJLPSKEnsxbo64y0OGPPYc"
# Events
@bot.event
async def on_ready():
   
    await bot.change_presence(status=discord.Status.online)
    print('bitch im online')
##help

bot.run(token,bot=False,)

