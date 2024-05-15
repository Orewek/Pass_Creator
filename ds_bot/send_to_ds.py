import discord

from ds_bot.dstoken import ds_token


def bot(txt_path: str) -> None:
    """turning on the bot, sending the .txt"""
    client = discord.Client()

    @client.event
    async def on_ready() -> None:
        # waiting when bot will log into discord
        print('We have logged in as {0.user}.'.format(client))

    @client.event
    async def on_message(message: any) -> None:
        if message.author == client.user:
            # waiting when user will type smth in chat
            return

        if message.channel.name == 'bot':
            if message.content == 'info' or message.content == 'help':
                await message.channel.send('write file or send')
            # sending .txt with our passwords
            if message.content == 'send' or message.content == 'file':
                await message.channel.send(file=discord.File(txt_path))

    client.run(ds_token)
