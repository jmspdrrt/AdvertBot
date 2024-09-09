import discord
from discord.ext import commands
import os

# Create bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load all cogs
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Load cogs from the cogs folder
bot.load_extension('cogs.advertisement')
bot.load_extension('cogs.ad_manager')  # Load the new cog

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
