import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import random

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(intents=intents)
EDIT_PERMISSION = 1024
#ADMINISTRATOR_PERMISSION = nextcord.Permissions(administrator=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(BOT_TOKEN)
