import discord
from discord.ext import commands
from libs import env,gpt
import json


TOKEN = env.load('BOT.TOKEN')

CHANNEL_ID = env.load('CH.WMSGPT_BETA')
# CHANNEL_ID = env.load('CH.DEV')

SERVER_ID = env.load('SERVER.ID')
# SERVER_ID = env.load('SERVER.ID_CERT')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild = bot.get_guild(int(SERVER_ID))
    members = guild.members
    user_names = [member.display_name for member in members]
    print(user_names)

    # Save user_names to a JSON file
    with open('user_list.json', 'w') as f:
        json.dump(user_names, f)

bot.run(TOKEN)
