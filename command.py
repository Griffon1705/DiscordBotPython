import discord

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
        embed.add_field(name=c.trigger , value=c.desc, inline=False)

    await message.channel.send(embed=embed)


COMMANDS = [
    command("help", showCommand, "Shows list of all the commands."),
    command("hello", greeting, "Greets the player."),
    command("hello!", greetingExtended, "Greets the player with a mention.")
]
