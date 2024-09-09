import discord
from discord.ext import commands, tasks
import random
import asyncio

class AdvertisementCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.advertisement_loop.start()

    @tasks.loop(hours=1)
    async def advertisement_loop(self):
        await self.send_advertisement()

    async def send_advertisement(self):
        # Read adverts from file
        with open("adverts.txt", "r") as file:
            adverts = file.readlines()

        if adverts:
            # Choose a random advert
            advert = random.choice(adverts)

            # Define the channel where the advert should be sent
            channel = self.bot.get_channel(YOUR_CHANNEL_ID)

            if channel:
                await channel.send(advert)

    @advertisement_loop.before_loop
    async def before_advertisement_loop(self):
        # Wait until the bot is ready before starting the loop
        await self.bot.wait_until_ready()

# This function is needed to load the cog in bot.py
async def setup(bot):
    await bot.add_cog(AdvertisementCog(bot))
