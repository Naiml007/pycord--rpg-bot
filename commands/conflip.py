import random
from discord.ext import commands

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="coinflip", description="Flip a coin! (Heads or Tails)")
    async def coinflip(self, ctx):
        """Flips a coin and returns the result (Heads or Tails)."""

        # Generate a random number (0 or 1)
        flip_result = random.randint(0, 1)

        # Translate the number to heads or tails
        if flip_result == 0:
            result = "Heads"
        else:
            result = "Tails"

        # Send the result to the user
        await ctx.respond(f"You flipped a coin and it landed on {result}!")

def setup(bot):
    bot.add_cog(Coinflip(bot))
