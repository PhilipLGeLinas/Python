# bot.py
import os
import destiny
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        for member in guild.members:
            print(f'{member.name}\n')

    await destiny.update_account_stats('philiplgelinas#6699')


# client.loop.create_task(update_accounts())
client.run(TOKEN)

