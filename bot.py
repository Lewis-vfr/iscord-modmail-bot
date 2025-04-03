import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # Haalt token op van Railway-variables

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online als {bot.user}")

bot.run(TOKEN)
