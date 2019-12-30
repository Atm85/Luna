from discord.ext import commands
from utils.FileManager import FileManager
from utils.ImageProcessor import ImageProcessor


class MemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not member.avatar_url == "":
            avatar = member.avatar_url
        else:
            avatar = member.default_avatar_url

        key = str(member.guild.id)
        settings = FileManager.read("settings.json")
        channel = member.guild.get_channel(int(settings[key]["channel"]))
        message = settings[key]["message"]
        format_msg = message. \
            replace("MEMBER", member.name). \
            replace("SERVER", member.guild.name). \
            replace("MENTION", member.mention). \
            replace("COUNT", str(len(channel.guild.members)))
        if settings[key]["image"] is not None:
            await ImageProcessor.upload(avatar, key, channel, format_msg)
        else:
            await channel.send(format_msg)


def setup(bot):
    bot.add_cog(MemberJoin(bot))
