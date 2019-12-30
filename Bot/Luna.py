import discord
from discord.ext import commands
from utils.Logger import Logger
from utils.FileManager import FileManager as File
import json

token = ""
prefix = ""


# returns console logger
def getlogger() -> Logger:
    return Logger()


# registers bot credentials
try:
    config = File.read("config.json")
    token = config["token"]
    prefix = config["prefix"]
except FileNotFoundError:
    getlogger().error("Default config not found! creating blank config.")
    with open("config.json", "w+") as f:
        configData = {"token": "", "prefix": ""}
        json.dump(configData, f, indent=4)

# register server message settings
try:
    settings = File.read("settings.json")
except FileNotFoundError:
    with open("settings.json", "w+") as newFile:
        settingsData = {}
        json.dump(settingsData, newFile, indent=4)


# returns bot auth token
def gettoken() -> str:
    return token


# registers bot command prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))

# remove default help command to create my own ;)
bot.remove_command('help')


# register bots startup methods
@bot.event
async def on_ready():
    getlogger().info("Preparing Bot Extensions!")
    if __name__ == "__main__":
        data = File.read("extensions.json")
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game("./help"))
        for ext in data["extensions"]:
            try:
                bot.load_extension(ext)
                getlogger().info("{} Was loaded successfully!".format(ext))
            except Exception as error:
                getlogger().error("{} Could not be loaded: [{}]".format(ext, error))


# activates bot with error handling
try:
    try:
        bot.loop.run_until_complete(bot.login(token=gettoken(), bot=True))
        try:
            bot.loop.run_until_complete(bot.connect(reconnect=True))
        except discord.GatewayNotFound:
            getlogger().error("There is an discord api outage! try again later.")
        except discord.ConnectionClosed:
            getlogger().error("discord web-socket connection has been terminated!")
    except discord.LoginFailure:
        getlogger().error("Failed to login to discord! perhaps your 'token' is incorrect.")
    except discord.HTTPException as e:
        getlogger().error(e.text)

except KeyboardInterrupt:
    getlogger().error("discord web-socket connection has been terminated!")
    bot.loop.run_until_complete(bot.logout())
finally:
    bot.loop.close()
