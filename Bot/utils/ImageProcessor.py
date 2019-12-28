import discord
import aiohttp
from PIL import Image, ImageDraw
from io import BytesIO


class ImageProcessor:

    @staticmethod
    async def download_from_obj(attachment, name, path):
        await attachment.save(fp=path+name+".png", use_cached=True)

    @staticmethod
    async def upload(avatar, key, channel, message):
        async with channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(str(avatar)) as image:
                    result = await image.read()

                with Image.open(BytesIO(result)) as avatar:
                    buffer = BytesIO()
                    avatar = avatar.resize((500, 500))
                    size = (avatar.size[0] * 3, avatar.size[1] * 3)
                    mask = Image.new("L", size, 0)
                    draw = ImageDraw.Draw(mask)
                    draw.ellipse((0, 0) + size, fill=255)
                    mask = mask.resize(avatar.size, Image.ANTIALIAS)
                    avatar.putalpha(mask)
                    background = Image.open("images/" + key + ".png")
                    background.paste(avatar, (710, 290), avatar)
                    background.save(buffer, "png")
                    buffer.seek(0)

                file = discord.File(fp=buffer, filename=key + ".png")
                await channel.send(content=message, file=file)

# formula for vertical positioning
# -
#
# formula for horizontal positioning
# -
#
# formula for avatar size
# -
#

