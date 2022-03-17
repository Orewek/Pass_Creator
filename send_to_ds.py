import discord
from dstoken import ds_token

client = discord.Client()


@client.event
async def on_ready():
    # waiting when bot will log into discord
    print('We have logged in as {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        # waiting when user will type smth in chat
        return

    path = r"D:\passwords.txt"
    if (True):
        # sending .txt with our passwords
        await message.channel.send(file=discord.File(path))

client.run(ds_token)
