#This Discord bot will have people split into balanced teams
import os
import discord

token = os.environ["DISCORD_TOKEN"]
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.find("!ping") != -1:
        await message.channel.send("pong")

client.run(token)