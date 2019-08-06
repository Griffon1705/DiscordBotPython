import discord, json
import urllib.request
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError

API_URL = "http://127.0.0.1:5000"

class command:

    def __init__(self, trigger, function, desc):
        self.trigger = trigger
        self.function = function
        self.desc = desc




async def greeting(message):
    await message.channel.send("Hellow")

async def greetingExtended(message):
    await message.channel.send("Hellow, {}".format(message.author.mention))

async def showCommand(message):

    embed = discord.Embed(title="Commands", description="List of all the commands: ")

    for c in COMMANDS:
        if c.desc != "":
            embed.add_field(name=PREFIX+c.trigger , value=c.desc, inline=False)

    await message.channel.send(embed=embed)

async def getDanceGif(message):

    try:
        req = urllib.request.urlopen(urlparse(API_URL+"/gif/random").geturl(), timeout=5)

    except (HTTPError, URLError) as error:
        await message.channel.send("Oops..., something broke.")
    else:
        if req.getcode() == 200:
            data = json.loads(req.read())
            await message.channel.send(data["content"])
        else:
            await message.channel.send("Oops..., something broke.")



COMMANDS = [
    command("help", showCommand, "Shows list of all the commands."),
    command("hello", greeting, "Greets the player."),
    command("hello!", greetingExtended, "Greets the player with a mention."),
    command("dance", getDanceGif, "")
]

PREFIX = "."
