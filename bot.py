# Pokemon Bot 

import pokemon
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('the bot is ready')

@client.event
async def on_member_joint(member):
    print('Trainer {member} has joined the server.')

@client.event
async def on_member_remove(member):
    print('Trainer {member} has left the server.')



@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def attack_vas(ctx):
    await ctx.send(f'Vaclav is dead')
@client.command()
async def attack_sean(ctx):
    await ctx.send(f'Sean is dead')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):

    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Qestion: {question}\nAnswer: {random.choice(responses)}')











client.run('NzQxMzkwNTMwMDE3MDk5ODE2.Xy23vA.kG1gvzG0SJX2n6GHis43nBqjFdc')




