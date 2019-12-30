import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def info(self, ctx):
        embed = discord.Embed(
            color=12632256,
            title="Luna bot v2.0",
            description="Welcome new members with style! overlay new member's avatar over a custom background image. Change the avatars position to fit your needs!"
        )
        embed.add_field(name="Bot author", value="<@287682736104275968>")
        await ctx.message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
