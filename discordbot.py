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
        await message.channel.send(f'🐢  🎀  𝒯🌺𝓃𝓎 𝒯🍬𝓃𝓎 𝒮🍬𝓊𝓅𝑒𝓇 𝒜𝒾𝓂𝑒 𝒮🌞𝓊𝓅𝑒𝓇 𝒮𝒶𝓃𝓈 𝑀🍑𝒹é𝓇𝒶𝓉𝒾🍪𝓃  🎀  🐢')
        return

client.run(TOKEN)