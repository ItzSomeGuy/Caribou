import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix='~', intents=discord.Intents.all())
TOKEN = os.getenv('TOKEN')


@client.event
async def on_ready():
    print(f'{client.user} is online')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'loaded {filename[:-3]}')

client.run(TOKEN)
