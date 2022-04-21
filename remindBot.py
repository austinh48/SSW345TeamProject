import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


from config import *

#firebase stuff doesn't work yet
#credentials for firebase
cred = credentials.Certificate(firebase_config)
databaseApp = firebase_admin.initialize_app(cred, {
    'databaseURL' : databaseUrl
})


#gets bot/client object from discord.py
Client = discord.Client()

#needed for commands
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


#add assignment command
@bot.command()
async def add(assignment, Name, dueDate, priority):
    await assignment.send('Assignment added')



#test firebase command - doesn't work yet
@bot.command(pass_context=True)
async def writeTest(ctx):
    color = input("Pick a color")
    user = ctx.message.author
    ref = db.reference(f"")
    ref.update({
        user : {
            "Color" :str(color)
        }
    })


bot.run(token)