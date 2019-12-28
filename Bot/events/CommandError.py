from discord.ext import commands
from utils.Logger import Logger


class CommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            getlogger().error(error)


def getlogger() -> Logger:
    return Logger()


def setup(bot):
    bot.add_cog(CommandError(bot))
