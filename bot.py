import requests
import discord
from keep_alive import keep_alive
import os
import json

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('#count'):
        await message.channel.send(1)
    else:
        special_message = '%20'.join((message.content).split(' '))

        res = requests.get(
            f"http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg={special_message}"
        )
        actual_message = res.content.decode()
        repliable = json.loads(actual_message)
        if 'Acobot Team' in repliable['cnt']:
            repliable = repliable['cnt'].replace('Acobot Team', "Arcenide")
        elif 'female' in repliable['cnt'] and 'really' not in repliable['cnt']:
            repliable = repliable['cnt'].replace('female', 'male')
        elif 'ZackyBot' in repliable['cnt']:
            repliable = repliable['cnt'].replace('ZackyBot', 'Lobdha')
            if 'common' in repliable:
                repliable = repliable['cnt'].replace('common', 'uncommon')
        elif "Don't forget to recommend me to your friends." in repliable[
                'cnt']:
            repliable = repliable['cnt'].replace(
                "Don't forget to recommend me to your friends.", '')
        elif "arcenide" in message.content and '?' in message.content:
            repliable = 'He is my creator and I obey him so much'
        elif "That's why many people chat with me everyday." in repliable[
                'cnt']:
            repliable = repliable['cnt'].replace(
                "That's why many people chat with me everyday.",
                "That's why you like me!")
        elif "You can turn me off by clicking the “X” on the top-right." in repliable[
                'cnt']:
            repliable = repliable['cnt'].replace(
                "You can turn me off by clicking the “X” on the top-right.",
                "Okay I stopped!")
        elif "I'm a virtual chat bot. You can chat with me." in repliable[
                'cnt']:
            await message.channel.send(file=discord.File('myImage.jpg'))
            repliable = repliable['cnt']
        elif "my" in message.content and 'name' in message.content and '?' in message.content:
            repliable = "Yes, your name is jemi. Arcenide told me"

        elif "Do you want me to tell you a joke?" in repliable['cnt']:
            repliable = "Hello, jemi! Do you want me to tell you a joke?"
        elif "Where is your creator" in message.content:
            repliable = "He is developing me in replit.com"
        elif "That's one of reasons why I'm getting more and more popular." in repliable[
                'cnt']:
            repliable = repliable['cnt'].replace(
                "That's one of reasons why I'm getting more and more popular.",
                "That's why you are liking me more and more!")
        else:
            repliable = repliable['cnt']

        await message.reply(repliable)


keep_alive()

client.run(os.getenv('DISCORD_TOKEN'))
