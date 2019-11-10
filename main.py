#This Discord bot will have people split into balanced teams
import os
import discord

token = os.environ["DISCORD_TOKEN"]
client = discord.Client()

waitlist = {}
queue_size = [0,0]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    """This method will deal with all messages in the server"""
    if message.content.find("!queue") != -1 and not message.author.bot: #To create a queue to split people into teams
        try:
            arr = str(message.content).split(" ")
            queue_size[0] = int(arr[1])
            queue_size[1] = int(arr[2])
            await message.channel.send("Queue successfully created\nParticipants may now register")
        except:
            if not message.author.bot:
                await message.channel.send("Unable to create Teams\nInvalid Command\nFormat: !queue #_of_Teams #_of_Team_Members\n\nEx: !queue 2 5\nCreates two teams of 5")



    elif message.content.find("!show queue") != -1 and not message.author.bot:#To see who is in the queue
        try:
            queue = "These are the people in the queue:"
            if len(waitlist)==0:
                await message.channel.send("There is no one in the queue")
            else:
                for member in waitlist:
                    queue += "\n"+member
                await message.channel.send(queue)
        except:
            if not message.author.bot:
                await message.channel.send("Unable to show who is in the queue")



    elif message.content.find("!register") != -1 and not message.author.bot:
        try:
            if message.author.name in waitlist:
                await message.channel.send(str(message.author.mention)+" is already registered\nRegistration Denied")
            else:
                arr = str(message.content).split(" ")
                waitlist[str(message.author.name)]=(arr[1], arr[2])
                await message.channel.send(str(message.author.mention) + " you are registered")
        except:
            await message.channel.send("Invalid command\nFormat: !register Rank LP\n\nEx: !register g4 50\nRegister as a Gold 4 50 LP player")



    elif message.content.find("!unregister") != -1 and not message.author.bot:
        try:
            for member in waitlist:
                if str(message.author.name) == member:
                    waitlist.pop(member)
                    await message.channel.send(str(message.author.name)+" is successfully removed from the queue")
                    break
        except:
            if not message.author.bot:
                await message.channel.send("Unable to remove from registration")

client.run(token)