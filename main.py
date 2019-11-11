#This Discord bot will have people split into balanced teams
import os
import discord


token = os.environ["DISCORD_TOKEN"]
client = discord.Client()
waitlist = {}

def findValue(rank):
    """
    Calculates how good a member is using their rank
    rank = ("rank","lp")
    """
    value = 100
    arr = list(rank[0])
    if "i" in arr or "I" in arr:
        if arr[1] == "4":
            value = value * .0 + ((int(rank[1])/100)*.048)
        elif arr[1] == "3":
            value = value * .048 + ((int(rank[1])/100)*.26)
        elif arr[1] == "2":
            value = value * .308 + ((int(rank[1])/100)*.59)
        elif arr[1] == "1":
            value = value * .898 + ((int(rank[1]) / 100)*.91)

    elif "b" in arr or "B" in arr:
        if arr[1] == "4":
            value = value * 1.808 + ((int(rank[1])/100)*2)
        elif arr[1] == "3":
            value = value * 3.808 + ((int(rank[1])/100)*2.3)
        elif arr[1] == "2":
            value = value * 6.108 + ((int(rank[1])/100)*3.8)
        elif arr[1] == "1":
            value = value * 9.908 + ((int(rank[1]) / 100)*5.8)

    elif "s" in arr or "S" in arr:
        if arr[1] == "4":
            value = value * 15.708 + ((int(rank[1])/100)*8.8)
        elif arr[1] == "3":
            value = value * 24.508 + ((int(rank[1])/100)*6.8)
        elif arr[1] == "2":
            value = value * 31.308 + ((int(rank[1])/100)*8.5)
        elif arr[1] == "1":
            value = value * 39.808 + ((int(rank[1]) / 100)*7.7)

    elif ("g" in arr or "G" in arr) and not ("m" in arr or "M" in arr):
        if arr[1] == "4":
            value = value * 47.008 + ((int(rank[1])/100)*14)
        elif arr[1] == "3":
            value = value * 61.008 + ((int(rank[1])/100)*7.7)
        elif arr[1] == "2":
            value = value * 68.708+ ((int(rank[1])/100)*6.7)
        elif arr[1] == "1":
            value = value * 75.408 + ((int(rank[1]) / 100)*4.2)

    elif "p" in arr or "P" in arr:
        if arr[1] == "4":
            value = value * 79.608 + ((int(rank[1])/100)*8.5)
        elif arr[1] == "3":
            value = value * 88.108 + ((int(rank[1])/100)*3.1)
        elif arr[1] == "2":
            value = value * 91.208 + ((int(rank[1])/100)*1.9)
        elif arr[1] == "1":
            value = value * 93.108 + ((int(rank[1]) / 100)*1.9)

    elif "d" in arr or "D" in arr:
        if arr[1] == "4":
            value = value * 95.008 + ((int(rank[1])/100)*2.2)
        elif arr[1] == "3":
            value = value * 97.208 + ((int(rank[1])/100)*.77)
        elif arr[1] == "2":
            value = value * 97.978 + ((int(rank[1])/100)*.36)
        elif arr[1] == "1":
            value = value * 98.338 + ((int(rank[1]) / 100)*.19)

    elif ("m" in arr or "M" in arr) and not("g" in arr or "G" in arr):
        value = value * 98.528

    elif ("g" in arr or "G" in arr) and ("m" in arr or "M" in arr):
        value = value * 98.587

    elif "c" in arr or "C" in arr:
        value = value * 98.937

    else:
        value = 5000

    return value

def findTeamValue(team):
    value = 0
    for member in team:
        value += float(team[member])

    return value


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    """This method will deal with all messages in the server"""
    global waitlist
    if message.content.find("!show queue") != -1 and not message.author.bot:#To see who is in the queue
        try:
            queue = "These are the people in the queue:"
            if len(waitlist) == 0:
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

    elif message.content.find("!make teams") != -1 and not message.author.bot:
        team1 = {}
        team2 = {}

        arr = []

        for member in waitlist:
            arr.append(member)

        for num in range(len(arr) - 1, 0, -1):
            for i in range(num):
                if findValue(waitlist[arr[i]]) > findValue(waitlist[arr[i + 1]]):
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp

        for member in arr:
            if findTeamValue(team1) < findTeamValue(team2) and len(team1)<5:
                team1[member] = findValue(waitlist[member])
            elif len(team2) < 5:
                team2[member] = findValue(waitlist[member])

        team1list = "Team 1:"
        for member in team1:
            team1list += "\n" + member

        team2list = "\n\nTeam 2:"
        for member in team2:
            team2list += "\n" + member

        await message.channel.send(team1list+team2list)
        waitlist = {}

client.run(token)