from discord.ext import commands
from utils.FileManager import FileManager
from utils.ImageProcessor import ImageProcessor

import asyncio


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def image(self, ctx):
        if not ctx.message.author.guild_permissions.administrator or (ctx.message.author.id == 287682736104275968):
            await ctx.message.channel.send("You do not have permission to use this command!")
        else:
            await ctx.message.channel.send("Upload banner image to use, supports images of ANY dimensions")
            key = str(ctx.message.guild.id)
            settings = FileManager.read("settings.json")
            settings[key]["setup_mode"] = 1
            FileManager.save(settings, "settings.json")

    @commands.Cog.listener()
    async def on_message(self, message):
        key = str(message.guild.id)
        settings = FileManager.read("settings.json")
        if not message.author.bot:
            if message.author.guild_permissions.administrator:
                if settings[key]["setup_mode"] == 1:
                    if message.attachments:
                        settings[key]["setup_mode"] = 0
                        att = message.attachments[0]
                        FileManager.save_default("settings.json", key)
                        settings[key]["image"] = True
                        FileManager.save(settings, "settings.json")
                        await ImageProcessor.download_from_obj(att, key, "images/")
                        await message.channel.send("Image set!, run command './test' to preview")


def setup(bot):
    bot.add_cog(Image(bot))
