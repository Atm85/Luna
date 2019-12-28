from discord.ext import commands
from utils.FileManager import FileManager
import discord
import asyncio


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def message(self, ctx):
        key = str(ctx.message.guild.id)
        FileManager.save_default("settings.json", key)
        settings = FileManager.read("settings.json")

        def get_response(response):
            settings[key]["message"] = response.content
            return response.author == ctx.message.author

        if not ctx.message.author.guild_permissions.administrator:
            await ctx.message.channel.send("You do not have permission to use this command!")
        else:
            embed = discord.Embed(
                color=0x2ecc71,
                title="message keywords"
            )
            embed.add_field(name="MEMBER", value="members username")
            embed.add_field(name="MENTION", value="mention new user")
            embed.add_field(name="SERVER", value="servers name")
            embed.add_field(name="COUNT", value="membercount")
            await ctx.message.channel.send("Please send the message you wist to use! time-out in 30s", embed=embed)
            try:
                await self.bot.wait_for("message", check=get_response, timeout=30.0)
                message = settings[key]["message"]
                format_msg = message.replace("MEMBER", ctx.message.author.name).replace("SERVER", ctx.message.guild.name).replace("MENTION", ctx.message.author.mention)
                embed = discord.Embed(title=format_msg)
                await ctx.message.channel.send("message has been set as...", embed=embed)
                FileManager.save(settings, "settings.json")
            except asyncio.TimeoutError:
                await ctx.message.channel.send("Timed-out! run command again")


def setup(bot):
    bot.add_cog(Message(bot))
