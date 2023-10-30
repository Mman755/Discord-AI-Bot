import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import random
import TextualAPI
import ImageAPI

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(intents=intents)
EDIT_PERMISSION = 1024
#ADMINISTRATOR_PERMISSION = nextcord.Permissions(administrator=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(guild_ids=[GUILD_ID], name="ask_question", description="Ask a question, anything!")
async def question(interaction: nextcord.Interaction, question):
    await interaction.response.defer()
    response = TextualAPI.get_response(question)
    truncated_response = response[:1900] + '...' if len(response) > 1900 else response
    await interaction.followup.send(truncated_response)

@bot.slash_command(guild_ids=[GUILD_ID], name="describe_image", description="Describe me an image and I will draw it for you!")
async def question(interaction: nextcord.Interaction, description):
    await interaction.response.defer()
    response = ImageAPI.get_image(description)
    await interaction.followup.send(response)

bot.run(BOT_TOKEN)
