import discord
from discord.ext import commands
from keep_alive import keep_alive
import os  # Default module

from dotenv import load_dotenv

load_dotenv()  # Load environment variables
intents = discord.Intents()
intents.message_content = True

# bot = bridge.Bot(command_prefix="!", intents=intents)

# Set the command prefix
bot = commands.Bot(command_prefix="n!")

# Load commands from separate files
cogs_path = "commands"
for filename in os.listdir(cogs_path):
    if not filename.endswith(".py"):
        continue  # Skip non-Python files
    import_path = f"{cogs_path}.{filename[:-3]}"
    bot.load_extension(import_path)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    keep_alive()

bot.run(os.getenv("TOKEN"))
