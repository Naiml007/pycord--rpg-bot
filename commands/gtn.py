import random
from discord.ext import commands

class Gtn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="gtn", description="Guess the Number game (1-10)")
    async def gtn(self, ctx):
        # Generate a random number
        secret_number = random.randint(1, 10)

        # Send initial message
        await ctx.respond("I'm thinking of a number between 1 and 10. Guess what it is!")

        # Track number of guesses
        guesses = 0

        # Loop for guess attempts
        while True:
            guesses += 1

            # Wait for user's guess
            def check(message):
                return message.author == ctx.author and message.content.isdigit()

            guess_message = await self.bot.wait_for("message", check=check)
            guess = int(guess_message.content)

            # Check if the guess is correct
            if guess == secret_number:
                await ctx.respond(f"You guessed it in {guesses} tries! ")
                break  # Exit the loop if guess is correct

            # Provide feedback based on the guess
            elif guess < secret_number:
                await ctx.respond("Too low! Try again.")
            else:
                await ctx.respond("Too high! Try again.")

def setup(bot):
    bot.add_cog(Gtn(bot))
