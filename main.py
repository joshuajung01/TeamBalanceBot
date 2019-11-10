#This Discord bot will have people split into balanced teams
import os
import discord
from boto.s3.connection import S3Connection

token = S3Connection(os.environ['DISCORD_TOKEN'])

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

async def onMessage(message):
    if message.author == client.user:
        return
    if message.content == "ping"
        message.channel.send("pong")

client.run(token)