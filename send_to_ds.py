import discord
from dstoken import ds_token

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    path = r"C:\Users\D.Charykov\!prog\vscode\pass_save.txt"
    if (True):
        await message.channel.send(file=discord.File(path))

client.run(ds_token)
