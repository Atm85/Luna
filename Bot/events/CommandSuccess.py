from discord.ext import commands
from utils.Logger import Logger


class CommandSuccess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        getlogger().info("{} executed command '{}{}' in server '{}'".format(ctx.author, ctx.prefix, ctx.command, ctx.guild))


# returns console logger
def getlogger() -> Logger:
    return Logger()


def setup(bot):
    bot.add_cog(CommandSuccess(bot))
