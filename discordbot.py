import sys
import discord

TOKEN = '' ;
f=open("TOKEN","r")
TOKEN=f.read()
    

client = discord.Client()

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'ping':
        await message.channel.send(f'pong')
        return
    if message.content.lower() == 'pong':
        await message.channel.send(f'ping')
        return
    if message.content.lower() == 'yo':
        await message.channel.send(f'Yo {message.author.display_name} ?')
        return
    if message.content.lower() == 'jan':
        await message.channel.send(f'')
        return
    if message.content.lower() == 'prout':
        await message.channel.send(f'PROUT')
        return
    if message.content.lower() == 'tony':
        await message.channel.send(f'๐ข  ๐  ๐ฏ๐บ๐๐ ๐ฏ๐ฌ๐๐ ๐ฎ๐ฌ๐๐๐๐ ๐๐พ๐๐ ๐ฎ๐๐๐๐๐ ๐ฎ๐ถ๐๐ ๐๐๐นรฉ๐๐ถ๐๐พ๐ช๐  ๐  ๐ข')
        return

client.run(TOKEN)