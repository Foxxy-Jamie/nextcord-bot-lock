import aiosqlite
import nextcord
from nextcord.ext import commands
from LockBot.exceptions import BOTLOCK, LockedBot

def locked():
    async def check_locks(ctx):
        async with aiosqlite.connect('lock.db') as db:
            async with db.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS bot_lock(channel INTEGER, guild INTEGER)")
                
                await cursor.execute("SELECT channel FROM bot_lock WHERE guild = ?", (ctx.guild.id,))
                check1 = await cursor.fetchone()
                if check1 == None:
                    return True
                elif check1[0] != ctx.channel.id:
                    raise BOTLOCK(commands.CheckFailure)
                else:
                    return True
    return commands.check(check_locks)
