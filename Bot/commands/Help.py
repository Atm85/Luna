import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        if ctx.message.author.avatar_url == "":
            icon_url = ctx.message.author.default_avatar_ur
        else:
            icon_url = ctx.message.author.avatar_url

        embed = discord.Embed(
            color=12632256
        )
        embed.set_author(name="{}".format(ctx.message.author), icon_url=icon_url)
        embed.add_field(name="./help", value="displays this help page", inline=True)
        embed.add_field(name="./channel", value="sets channel to use to send messages in", inline=True)
        embed.add_field(name="./message", value="sets what message I should send in the set channel", inline=True)
        embed.add_field(name="./image", value="sends a banner image overlay with the message", inline=True)
        embed.add_field(name="./pos", value="modifies avatar position (left, center, right)", inline=True)
        embed.title = "Mellon Bot help page\n-------------------------"

        await ctx.message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
