import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import random
import TextualAPI
import ImageAPI


# Load the env variables and extract them to usable variables
load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID')) # Guild ID is the id of the server in which the bot is active

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(intents=intents)
EDIT_PERMISSION = 1024

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(guild_ids=[GUILD_ID], name="ask_question", description="Ask a question, anything!")
async def question(interaction: nextcord.Interaction, question):
    """
    Interacts with the general OpenAI API and passes the user question and retrieves response

    :param interaction: Interaction object representing the command invocation
    :param question: The prompt the user provides which is provided to the OpenAI API as param
    :return: None
    """
    await interaction.response.defer()
    response = TextualAPI.get_response(question)
    # Discord does not like big messages and has char limits, so this is done to prevent errors. Might not be the best way
    # but it works for now...
    truncated_response = response[:1900] + '...' if len(response) > 1900 else response
    await interaction.followup.send(truncated_response)

@bot.slash_command(guild_ids=[GUILD_ID], name="describe_image", description="Describe me an image and I will draw it for you!")
async def question(interaction: nextcord.Interaction, description):
    """
    Interacts with the Image API provided by OpenAI API and passes the description which is then used to generate an image

    :param interaction: Interaction object representing the command invocation
    :param description: The description provided by the user which is passed to the OpenAI DALL E API service
    :return: None
    """
    await interaction.response.defer()
    response = ImageAPI.get_image(description) # Retrieve the response from the API
    await interaction.followup.send(response) # Use followup send message instead of normal due to asynch behavior

bot.run(BOT_TOKEN)
