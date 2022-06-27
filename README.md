# **Nextcord-Bot-Lock**

[![Powered by Nextcord](https://custom-icon-badges.herokuapp.com/badge/-Powered%20by%20Nextcord-0d1620?logo=nextcord)](https://github.com/nextcord/nextcord "Powered by Nextcord Python API Wrapper")

This is a unofficial extension of Nextcord.py. This allows you to lock your bot to a certain Text channel, using MySql as a Database. The package is only in developing stage so there will be bugs. **This is only to lock bots to channels will not be increased to Roles**

### ***Please Note***
> The package will be continued but may be buggy and error based. As the package grows so shall the database. meaning more data can be stored.
## **Quick Example**

```py 
import nextcord
from nextcord.ext import commands
from LockBot.check import locked
import LockBot.exceptions

intents=intents=nextcord.Intents.all()
client = commands.Bot(command_prefix=commands.when_mentioned_or('b!', 'B!'), intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name='Visual Studio Code'))
    print(f"Logged in as: {client.user.name}")

# Example Error Handler For Package

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, LockBot.exceptions.BOTLOCK):
        await ctx.reply(error)

# Put locked() in the checks area just like commands.is_owner() 

@client.command()
@locked()
async def testloc(ctx):
    await ctx.reply("TestLoc seems to be working")

client.run("bot token")
```
