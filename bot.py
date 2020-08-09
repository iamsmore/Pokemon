"""Pokemon Bot 

Current Commands: 
    - _8ball (aliases: 8ball, test): returns random response
    - ping: Returns pong, with the current latency 
    - 

"""
from pokemon import * 
import discord, random
from discord.ext import commands
import json
import os


client = commands.Bot(command_prefix = '.')

Saph = Trainer([magikarp, magikarp], 'Vas', 2, 0)
iamsmore = Trainer([squirtle, magikarp], "Sean", 2, 0)
sputnicc = Trainer([charmander, charizard], 'Nic', 2, 0)



# Events

@client.event
async def on_ready():
    print('the bot is ready')

@client.event
async def on_member_join(member):

    print(f'Trainer {member} has joined the server.')

    #create dictionary to write
    test_dictionary = {"test":"test"}

    with open('trainer_log.py','a') as f:
        json.dump(test_dictionary,f)
        f.write(os.linesep)



@client.event
async def on_member_remove(member):
    print(f'Trainer {member} has left the server.')





# Commands


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def battle(ctx, loser):
    #battler = ctx.author.name 
    await ctx.send(sputnicc.attack(Saph))

@client.command()
async def attack_sean(ctx):
    await ctx.send(f'{ctx.author.name} is dead')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):

    responses = [
                    "Sorry fella, I don’t have the energy to pretend to like you today.",
                    "Umm...pardon me, I wasn’t listening. Can you repeat what you just said?",
                    "Ok.",
                    "That sounds weird coming from you. Am I? Am I Really?",
                    "Are you always such an idiot, or do you just show off when I’m around?",
                    "Whatever you say, hefe.",
                    "Sorry, I don’t understand what you’re saying. I don’t speak bullsh*t.",
                    "Did it hurt when you fell from heaven? If they ask you why, say: 'Cause it looks like you landed on your face!'",
                    "Awww...are you having a bad day? ",
                    "Thank you very much for thinking about me! Bye.",
                    "*Repeat what they just said back*",
                    "I hope your day is as pleasant as your personality!",
                    "Just so you know, this conversation is being recorded.",
                    "The jerk store called. They said they're all out of...you!",
                    "Your misguided opinion is false but cute.",
                    "Goodbye!",
                    "Cool story bro!",
                    "You know they can hear you, right?",
                    "It is kind of hilarious watching you try to fit your entire vocabulary into one sentence.",
                    "How is that supposed to make me feel?",
                    "There are some incredibly dumb people in this world. Thanks for helping me understand that.",
                    "Look, if I wanted to hear from an asshole, all I had to do was fart.",
                    "I've been called worse things by better people.",
                    "If ignorance is bliss, you must be the happiest person on the planet.", 
                    "You have your entire life to be a jerk. Why not take today off?", 
                    "Please cancel my subscription to your issues.", 
                    "I'm calling the cops.", 
                    "People like you are the reason I’m on medication.", 
                    "I don't care what everyone else says. I don't think you're that bad.", 
                    "May I ask you to stop talking. It smells really bad.", 
                    "Remember when I asked for your opinion? Well, me neither.", 
                    "Thanks for sharing. We’re all refreshed and challenged by your unique point of view.",
                    "Remember that time when I said you were cool? I lied.", 
                    "I have better things to do than listening to you.", 
                    "*Makes sustained eye contact and then licks lips*", 
                    "Your ass must be pretty jealous of all the shit that comes out of your mouth.", 
                    "You always bring me so much joy—as soon as you leave the room.", 
                    "Here’s a tissue, you have some sh*t on your lips.", 
                    "If you ran like your mouth, you’d be in good shape.", 
                    "Mirrors don’t lie, and lucky for you, they also don’t laugh.",
                    "Surprise me. Say something intelligent.", 
                    "Unless your name is Google, stop acting like you know everything.", 
                    "Roses are red; violets are blue. I have five fingers, and the third one is for you.", 
                    "I’d slap you, but that would be animal abuse.", 
                    "Talk to the hand!", 
                    "Wow, you’re really smart!"
]
    await ctx.send(f'Qestion: {question}\nAnswer: {random.choice(responses)}')


client.run('NzQxMzkwNTMwMDE3MDk5ODE2.Xy23vA.QysLvGPV1OLeADcsPCczN5pUgN4')




