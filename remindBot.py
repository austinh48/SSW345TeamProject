import discord
from discord.ext import commands

#gets bot/client object from discord.py
Client = discord.Client()

#needed for commands
intents = discord.Intents.default()
#intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#event listener that switches bot to online
@bot.event
async def on_ready(self):
    print(f'Logged on as {self.user}!')

@bot.command()
async def hi(test):
    await test.send('Hello')


bot.run('OTY2Mzk0NjgxNjIzNzE5OTQ2.YmBHLg.wCIy4uvOrZkMpaD29cC40XGReKk')