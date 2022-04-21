import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db


from config import *

#credentials for firebase
cred = credentials.Certificate(firebase_config)
databaseApp = firebase_admin.initialize_app(cred, {
    'databaseURL' : databaseUrl
})

dBase = firestore.client()

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



#test firebase write
@bot.command()
async def writeTest(ctx):
    doc_ref = dBase.collection(u'test').document(u'color')
    doc_ref.set({
        u'color': u'green'
    })

#test firebase read
#@bot.command()


bot.run(token)