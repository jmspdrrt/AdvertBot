import discord
from discord.ext import commands

class AdManagerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add_advert")
    @commands.has_role('Advert Manager')  # Role check to restrict access
    async def add_advert(self, ctx, *, advert: str):
        """Allows users with the 'Advert Manager' role to add new adverts."""
        # Append the new advert to the adverts.txt file
        with open("adverts.txt", "a") as file:
            file.write(advert + "\n")

        await ctx.send(f"Advert added: {advert}")

    @add_advert.error
    async def add_advert_error(self, ctx, error):
        """Error handler for the add_advert command."""
        if isinstance(error, commands.MissingRole):
            await ctx.send("You do not have the required role to add adverts.")
        else:
            await ctx.send(f"An error occurred: {str(error)}")

# This function is needed to load the cog in bot.py
async def setup(bot):
    await bot.add_cog(AdManagerCog(bot))
