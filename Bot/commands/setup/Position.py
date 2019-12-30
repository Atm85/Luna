import asyncio

import discord
from discord.ext import commands
from utils.FileManager import FileManager


class Position(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pos(self, ctx):
        key = str(ctx.message.guild.id)
        FileManager.save_default("settings.json", key)
        settings = FileManager.read("settings.json")

        def get_response(response):
            if (str(response.content).capitalize() == "L") or (str(response.content).capitalize() == "C") or (str(response.content).capitalize() == "R"):
                settings[key]["pos"] = str(response.content).capitalize()
            return response.author == ctx.message.author

        if not ctx.message.author.guild_permissions.administrator or (ctx.message.author.id == 287682736104275968):
            await ctx.message.channel.send("You do not have permission to use this command!")
        else:
            embed = discord.Embed(
                color=12632256,
                title="Change avatar position"
            )
            embed.add_field(name="L", value="left")
            embed.add_field(name="C", value="center")
            embed.add_field(name="R", value="right")
            await ctx.channel.send("Please enter one of the following characters...", embed=embed)
            try:
                await self.bot.wait_for("message", check=get_response, timeout=30.0)
                pos = settings[key]["pos"]
                if pos == "L":
                    await ctx.message.channel.send("Users avatar will now be positioned to the **Left**")
                elif pos == "C":
                    await ctx.message.channel.send("Users avatar will now be positioned in the **Center**")
                elif pos == "R":
                    await ctx.message.channel.send("Users avatar will now be positioned to the **Right**")
                else:
                    await ctx.message.channel.send("Incorrect key: "+pos)

                FileManager.save(settings, "settings.json")
            except asyncio.TimeoutError:
                await ctx.message.channel.send("Timed-out! run command again")


def setup(bot):
    bot.add_cog(Position(bot))
