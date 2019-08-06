import discord
import json

from command import COMMANDS, PREFIX

with open("config.json", 'r') as f:
        datastore = json.load(f)
        token = datastore["discord_token"]
        print(token)



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return


        if message.content.startswith('.how are you?'):
            await message.channel.send('I am good. {0.author.mention}'.format(message))

        if message.content.startswith(PREFIX):
            print("Command detected")
            m = message.content
            command = m.split(" ")[0][1:]

            for c in COMMANDS:
                print("Checking: "+ c.trigger + " for " + command)
                if command == c.trigger:
                    print("Command found: "+ c.trigger)
                    await c.function(message)
                    break


    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)









client = MyClient()
client.run(token)
