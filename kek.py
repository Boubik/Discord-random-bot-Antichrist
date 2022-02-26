import discord
import random
import config

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=config.easterEggText))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[-1] == config.questionDefinition:
        lol = random.randrange(2)
        if lol == 0:
            await message.channel.send(config.no)
        if lol == 1:
            await message.channel.send(config.yes)
        return
    if message.content[:6].lower() == config.multiDefinition:
        if message.content.lower() == config.easterEgg:
            await message.channel.send(config.easterEggText + ' ' + str(message.author.name) + '!')
            return
        else:
            text = message.content[7:]
            thinks = text.split(config.separator)
            await message.channel.send(thinks[random.randrange(len(thinks))])
            return

client.run(config.token)
