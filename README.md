# TeamBalanceBot for League of Legends 
This bot is to help make fair competitive custom matches amongst friends

TeamBalanceBot is...
- [x] Easy to use
- [x] Creates Fair Custom Teams
- [x] Prevents the Toxicty

## Contents
1. About TeamBalanceBot
2. Getting Started
3. About the Code
4. About Me

## About TeamBalanceBot
League of Legends is one of the world's most played video game. 
With over 80 million players, it has captivated the attention of PC gamers all over the world.  

One of the many game modes in League of Legends is custom matches. 
In custom matches 10 players get in a lobby and face off in a 5 v 5 match.  Since the teams need to be created manually, the teams are often unbalanced

### The Problem
Custom Matches in League of Legends matches are unfair and the matches are not competitive. 
This leads to toxicity and an overall negative experience playing the game.

### The Solution
TeamBalanceBot accounts for each player's skill level to make the most balanced teams possible for custom games.  
Originally I made the bot calculate each player's skill based off the rank linearly, but this is flawed because the learning curve of the game is not linear.
Instead, my bot now creates the teams by assining values to each player based on the percentile of their rank, so now each players rank scales accurately.
This data was collected online at [link](https://www.leagueofgraphs.com/rankings/rank-distribution)

TeamBalanceBot will use 10 registered players to form the "most fair" teams possible quickly, efficiently, and accurately.
This removes the hassle of trying to even out teams manually.  
Custom matches naturally become more competitive because the teams' overall skill level are similar

## Getting started

### Installation
Invite the bot to you server [here](https://discordapp.com/api/oauth2/authorize?client_id=642757039482994688&permissions=0&scope=bot)

### Commands 

Here are the commands to control TeamBalanceBot
- !register => Register to play in the custom game
- !unregister => Remove yourself from the custom game
- !remove => Allow mods to remove a person from the custom game
- !show queue => Shows who is registered to play in the custom game
- !make teams => Makes the two balanced teams for the custom game
- !clear => Clears the registration board
- !help => See the commands to control TeamBalanceBot

## About the Code

This discord bot obviously uses discord.py, an API wrapper for Discord.
The bot listens to the text channel. It scans each message for the commands listed above. 
If it finds a command it acts accordingly.

There are methods that are used to determine the value of each player and of the team. 
Each player is given a value based on the percentile of their rank with the highest ranked players having a value of 10000 and the lowest ranked players having a value of 0.
The value of a team is the sum of all the values of the players. 

The bot is hosted on Heroku. Heroku deploys the bot by using a worker.  This worker processes jobs and exeutes them according to our code. 

## About me 
Hi, my name is Joshua Jung, and I am a freshman computer science major at Texas A&M University.  
My inspiration for this bot was from my personal experience playing in League of Legends custom matches.
My friends and I would often play games together, but they always ended the same:

**PSHAW** "The teams weren't _fair!_", "You guys got _lucky_ you had ____ player", "Honestly my teamates are sooo **Trash**"

This type of toxic mentality and excuses were always prevelant at the end of your games.  
This would always happend because of our inability to make fair teams that would create competitive gameplay. 
With the TeamBalanceBot my friends and I are able to create fair teams, so that we can settle our differences and have an undisputed winner. 

Thanks for checking out TeamBalanceBot.  
It has a lot of room for improvement, but I tried my best to create a simple problem to an age-old problem.
It is my first time using Git extensively, and I learned a lot about coding from this experience.
I hope you enjoy using the bot.

I would like to thank Capsher Technology and the Aggie Coding Club for hosting the competition that my bot was entered in. 
