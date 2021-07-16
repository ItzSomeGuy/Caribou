import discord
import os
import threading
import csv
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

load_dotenv()

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')
TOKEN = os.getenv('TOKEN')

# I'm sure it's perfect
@client.event
async def on_ready():
    print(f'{client.user} is online')
    check_time()


# update members.csv data
def check_time():
    threading.Timer(60, check_time).start()

    now = datetime.now()

    current_time = now.strftime('%H:%M')

    if current_time == '04:00':
        update_member_data()


def update_member_data():
    for guild in client.guilds:
        guild_name = guild.name
        members = guild.members
        data = None

        for file in os.listdir('./data'):
            if file.endswith('-members.csv'):  # file name: guild_name-members.csv
                if file[:-12] == guild_name:  # file name: [guild_name]-members.csv
                    data = open(f'./data/{file}', 'r')  # sets data if file exists, is None if file does not exist

        if data is None:
            with open(f'./data/{guild_name}-members.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'ID', 'Roles', 'Insured', 'GE', 'GE_Multi', 'rank'])
                for member in members:
                    writer.writerow([member.name, member.id, member.roles, False, False, 1, 'None'])
        else:
            # store current CSV -> update name,roles,ge_multi -> override CSV
            dt = []
            reader = csv.reader(data)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                dt.append((row[3], row[4], row[6]))
            data.close()

            data = open(f'./data/{file}', 'w')
            writer = csv.writer(data)
            writer.writerow(['Name', 'ID', 'Roles', 'Insured', 'GE', 'GE_Multi', 'rank'])
            for i, member in enumerate(members):
                tp = dt[i]
                writer.writerow([member.name, member.id, member.roles, tp[0], tp[1], 1, tp[2]])
            data.close()


@client.command()
async def update(ctx):
    await ctx.message.delete()

    update_member_data()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'loaded: {filename}')

client.run(TOKEN)
