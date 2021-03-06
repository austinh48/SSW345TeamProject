import discord
from discord.ext import commands, tasks
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import threading

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

#prints to terminal when bot is online
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

#create an assignment
@bot.command()
async def add(ctx, assignmentName, dueDate, priority):
    #make a new assignment doc for each user
    doc_ref = dBase.collection(u'Assignments').document(assignmentName)
    doc_ref.set({
        u'Assignment Name': assignmentName,
        u'Due Date': dueDate,
        u'Priority': priority
    })
    #prints to terminal
    print("Adding assignment")

#list existing assignments
@bot.command()
async def list(ctx):
    #references the Assignments collection in firebase
    users_ref = dBase.collection(u'Assignments')
    docs = users_ref.stream()

    #prints the info from the firebase docs in the asignment category
    for doc in docs:
        #sends document info in discord without document id
        await ctx.send(f'{doc.id} : {doc.to_dict()}')
        #await ctx.send(f'{doc.id} : {doc.to_dict()}') will send with the document id

    #prints to terminal
    print("Listing Documents")

#completes an assignment and deletes it from the database
@bot.command()
async def completed(ctx, docName):
    #deletes the document that was specified by the docName
    dBase.collection(u'Assignments').document(docName).delete()
    await ctx.send("Good job! The assignment has been removed from your to do list.")

#deletes an assignment
@bot.command()
async def delete(ctx, docName):
    #deletes the document that was specified by the docName
    dBase.collection(u'Assignments').document(docName).delete()
    await ctx.send("The assignment has been deleted.")

#sends a notification
@tasks.loop(minutes=1)
async def notification():
    channel = bot.get_channel(966395861305278486)
    await channel.send("Test")

#put notification in this to run the notificaton event
@bot.event
async def on_ready():
    await checkTime()

#might have to make this a bot event
async def checkTime():
    threading.Timer(1, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current time: ", current_time)

    #checks time to send notifications
    if(current_time == '03:35:00'):
        channel = bot.get_channel(966395861305278486)
        await channel.send("Testing")

checkTime()

bot.run(token)