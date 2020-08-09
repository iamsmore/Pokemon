import discord, random, json, os
from pokemon import * 
from discord.ext import commands
from random_lists import *


# Opens pokemon_stats.json, creates a Pokemon object for each pokemon, stores all pokemon objects into 'pokemons{}'
with open('pokemon_stats.json') as json_file:
    pokemon_data = json.load(json_file) 
    pokemons = {}

    # For pokemon in the json file, create Pokemon Object
    for poke in pokemon_data:
        pokemons[poke['name']] = Pokemon(poke['name'],poke['level'], poke['type'], poke['max_health'], poke['current_health'], poke['ko'] )

# Opens trainer_log.json, creates a Trainer object for each trainer, stores all trainer objects into 'trainers{}'
with open('trainer_log.json') as json_file:
    trainer_data = json.load(json_file) 
    trainers = {}

    # For trainer in the json file, create Trainer object
    for trainer in trainer_data:
        trainer_poke_list = []
    
        for poke in trainer['pokemon_list']: # Creates list of pokemon objects, and stores into trainer_poke_list
            trainer_poke_list.append(pokemons[poke])
        
        trainers[trainer['name']] = Trainer(trainer_poke_list, trainer['name'],trainer['potions'], trainer['currently_active'])
#print(trainers)

client = commands.Bot(command_prefix = '.')
# ---------------------------------------------------------------------------------------------
# Events

@client.event
async def on_ready():
    print('the bot is ready')

@client.event
async def on_member_join(member):

    print(f'Trainer {member} has joined the server.')

    with open('trainer_log.json') as json_file:
        trainer_data = json.load(json_file)

    #need to give random starter pokemon
    new_trainer = { "pokemon_list": ["squirtle", "squirtle"],
        "name": f'{member}'[0:-5],
        "potions": 0, 
        "currently_active": 0 }


    trainer_data.append(new_trainer)

    #deletes content of the file
    f = open('trainer_log.json', 'r+')
    f.truncate(0)
    f.close()


    with open('trainer_log.json','w') as json_file:
        json.dump(trainer_data, json_file,indent=4)


@client.event
async def on_member_remove(member):
    print(f'Trainer {member} has left the server.')


# ---------------------------------------------------------------------------------------------
# Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def battle(ctx, loser):
    try: 
        battler = ctx.author.name 
        await ctx.send(trainers[battler].attack(trainers[loser]))

    except:
        await ctx.send('You cannot battke this person!')

@client.command()
async def attack_sean(ctx):
    await ctx.send(f'{ctx.author.name} is dead')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Qestion: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['baby'])
async def abg(ctx, *, question):
    await ctx.send(f'Your ABG is: {random.choice(girl_names)}')


client.run('')




