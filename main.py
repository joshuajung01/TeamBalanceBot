#This Discord bot will have people split into balanced teams
import os
import discord

token = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

async def onMessage(message):
    if message.author == client.user:
        return
    if message.content == "ping":
        message.channel.send("pong")

client.run(token)