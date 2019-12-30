from discord.ext import commands
from utils.FileManager import FileManager
from utils.ImageProcessor import ImageProcessor


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def test(self, ctx):
        key = str(ctx.message.guild.id)
        settings = FileManager.read("settings.json")
        if not ctx.message.author.guild_permissions.administrator:
            await ctx.message.channel.send("You do not have permission to use this command!")
        else:
            if not ctx.message.author.avatar_url == "":
                avatar = ctx.message.author.avatar_url
            else:
                avatar = ctx.message.author.default_avatar_url

            channel = ctx.message.guild.get_channel(int(settings[key]["channel"]))
            message = settings[key]["message"]
            format_msg = message.\
                replace("MEMBER", ctx.message.author.name).\
                replace("SERVER", ctx.message.guild.name).\
                replace("MENTION", ctx.message.author.mention).\
                replace("COUNT", str(len(channel.guild.members)))

            await ctx.message.channel.send("A test message was sent to the channel that was set!")
            if settings[key]["image"] is not None:
                await ImageProcessor.upload(avatar, key, channel, format_msg)
            else:
                await channel.send(format_msg)


def setup(bot):
    bot.add_cog(Test(bot))
