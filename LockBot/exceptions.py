from nextcord.ext.commands import CommandError

class LockedBot(CommandError):
    """Base Exception"""
    pass

class BOTLOCK(LockedBot):
    def __init__(self, argument: str) -> None:
        self.argument: str = argument
        super().__init__(f'Bot is Locked To a Channel Cant Send Messages...')