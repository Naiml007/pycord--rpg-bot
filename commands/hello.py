from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="hello", description="Say hello to the bot")
    async def hello(self, ctx):
        await ctx.respond(f"Hey there, {ctx.author.mention}!")

def setup(bot):
    bot.add_cog(Hello(bot))
