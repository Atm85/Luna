from colorama import init
from termcolor import colored
from datetime import datetime


class Logger:
    def __init__(self):
        init()

    @staticmethod
    def info(message):
        print("["+colored("Bot", "green")+"/"+colored("info", "green")+"] "+colored(message, "cyan"))

    @staticmethod
    def error(message):
        print("["+colored("Bot", "red")+"/"+colored("error", "red")+"] "+colored(message, "cyan"))

    @staticmethod
    def format_time():
        return "[{}]".format(datetime.utcnow())
