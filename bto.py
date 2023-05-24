import discord
from os import getenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Im ready to generate the text!!! {client.user}")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.startswith("/start"):
        await msg.channel.send("hi there, how i can help you ")

    if msg.content.startswith("generate"):
        await msg.channel.send("Generating text please wait....")

token = getenv("TOKEN")

client.run(token)