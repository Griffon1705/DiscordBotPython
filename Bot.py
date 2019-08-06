import discord

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

        if message.content.startswith('.hello'):
            await message.channel.send('Hello. i am a work in progress so this is the onlything i can say ._. {0.author.mention}'.format(message))


        if message.content.startswith('.help'):
            await message.channel.send('I can answer .Hello and .How are you? {0.author.mention}'.format(message))


        if message.content.startswith('.how are you?'):
            await message.channel.send('I am good. {0.author.mention}'.format(message))


    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)









client = MyClient()
client.run('NjA3MjYyNjk2MjQwNDQ3NjEz.XUhDfQ.pm0cKHFNyCFVCFjsnIkJRIQy0ag')
