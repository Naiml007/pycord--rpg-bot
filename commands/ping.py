from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Check the bot's latency.")
    async def ping(self, ctx):
        """A simple ping command to check the bot's latency."""
        latency = round(self.bot.latency * 1000)  # Calculate latency in milliseconds
        await ctx.respond(f"Pong! Latency is {latency}ms.")

def setup(bot):
    bot.add_cog(Ping(bot))
