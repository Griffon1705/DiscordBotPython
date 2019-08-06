
class command:

    def __init__(self, trigger, function):
        self.trigger = trigger
        self.function = function




async def greeting(message):
    await message.channel.send("Hellow")

async def greetingExtended(message):
    await message.channel.send("Hellow, {}".format(message.author.mention))

async def showCommand(message):
    await message.channel.send({
        embed: {
            title: "Commands",
            description: "All the commands:"
        }
    })

COMMANDS = [
    command("help", showCommand),
    command("hello", greeting),
    command("hello!", greetingExtended)
]
