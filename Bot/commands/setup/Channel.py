from discord.ext import commands
from utils.FileManager import FileManager
import asyncio


class Channel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def channel(self, ctx):
        key = str(ctx.message.guild.id)
        FileManager.save_default("settings.json", key)
        settings = FileManager.read("settings.json")

        def get_response(response):
            if response.channel_mentions:
                channel_id = response.content.strip("<#>")
                settings[key]["channel"] = channel_id
                return response.author == ctx.message.author

        if not ctx.message.author.guild_permissions.administrator:
            await ctx.message.channel.send("You do not have permission to use this command!")
        else:
            await ctx.message.channel.send("Please mention the channel you wist to use!")
            try:
                await self.bot.wait_for("message", check=get_response, timeout=30.0)
                channel = ctx.message.guild.get_channel(int(settings[key]["channel"]))
                await ctx.message.channel.send("{} has been set!".format(channel.mention))
                FileManager.save(settings, "settings.json")
            except asyncio.TimeoutError:
                await ctx.message.channel.send("Timed-out! run command again")


def setup(bot):
    bot.add_cog(Channel(bot))
