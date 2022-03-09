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
        text = message.content
        splited = text.split(" ")

        if splited[1].lower() == config.flip_a_coin_definition:
            await message.channel.send(random.choice(config.coin))
            return
        if len(splited) > 2:
            if splited[2].lower() == config.team or splited[2].lower() == config.teamr:
                if splited[2] == config.teamr:
                    kek = message.content.split(config.teamr+" ")
                else:
                    kek = message.content.split(config.team+" ")
                names = kek[1].split(config.separator)
                if splited[2] == config.teamr:
                    random.shuffle(names)
                names_len = len(names)
                for i in range((int(splited[1])-1)):
                    ar = []
                    for k in range(round(names_len/int(splited[1]))):
                        ar.append(names.pop(0))
                    await message.channel.send(ar)

                await message.channel.send(names)
                return
        if message.content.lower() == config.easterEgg:
            await message.channel.send(config.easterEggText + ' ' + str(message.author.name) + '!')
            return
        else:
            text = message.content[7:]
            thinks = text.split(config.separator)
            await message.channel.send(thinks[random.randrange(len(thinks))])
            return

client.run(config.token)
