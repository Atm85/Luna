import time
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.message.channel.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong! `{int(ping)}ms`")


def setup(bot):
    bot.add_cog(Ping(bot))
