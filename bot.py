import discord, random, json, os
from pokemon import * 
from discord.ext import commands
from random_lists import *
import random



# Opens pokemon_stats.json, creates a Pokemon object for each pokemon, stores all pokemon objects into 'pokemons{}'
with open('pokemon_stats.json') as json_file:
    pokemon_data = json.load(json_file) 
    pokemons = {}

    # For pokemon in the json file, create Pokemon Object
    for poke in pokemon_data:
        pokemons[poke['name']] = Pokemon(poke['name'],poke['level'], poke['type'], poke['max_health'], poke['current_health'], poke['ko'], poke['exp'] )

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

#generate list of pokemon that are entry level
entry_level_pokemon = []
for pokemon in pokemons.values():
    if pokemon.level == 1:
        print(pokemon.name)
        entry_level_pokemon.append(pokemon)

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

    #need to change taken variable of the randomly chosen pokemon
    random_index = random.sample(range(0,len(entry_level_pokemon) - 1),2)
    new_trainer_pokemon = []
    new_trainer_pokemon.append(entry_level_pokemon[random_index[0]])
    new_trainer_pokemon.append(entry_level_pokemon[random_index[1]])
    print(new_trainer_pokemon[0].name)
    print(new_trainer_pokemon[1].name)

    with open('pokemon_stats.json') as json_file:
        poke_data = json.load(json_file) 

    #update the availability status of both pokemon
    for pokemon in poke_data:
        if pokemon["name"] ==  new_trainer_pokemon[0].name:
            print("hallo")
            pokemon["taken"] = True
            #print(poke_data)

        if pokemon["name"] ==  new_trainer_pokemon[1].name:
            print("hello")
            print(pokemon["taken"])
            pokemon["taken"] = True
            print(pokemon["taken"])
            print(poke_data)

    #deletes content of the file
    p = open('poke_stats.json', 'r+')
    p.truncate(0)
    p.close()

    #writes to a new file for testing
    #with open('poke_stats.json','w') as json_file:
        #json.dump(poke_data, json_file,indent=4)



    #need to give random starter pokemon
    new_trainer = { "pokemon_list": [new_trainer_pokemon[0].name, new_trainer_pokemon[1].name],
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

@client.command() # Trainer command to attack another trainer
async def start_battle(ctx, loser):
    global LAST_TURN
    global START_BATTLE 

    try:
        if START_BATTLE == 1:
            return await ctx.send('Please wait for the current battle to finish before starting a new battle')

    except:
        try: 
            
            battler = ctx.author.name
            LAST_TURN = battler
            START_BATTLE = 1
            await ctx.send(f'----- {(trainers[battler].name).upper()} has decided to battle {(trainers[loser].name).upper()}! -----')
            await ctx.send(trainers[battler].attack(trainers[loser]))
            print(trainers[battler].pokemon_list[0])

        except:
            await ctx.send('You cannot battle this person!')

@client.command() # Trainer command to attack another trainer
async def battle(ctx, loser):
    global LAST_TURN
    global START_BATTLE 

    try:
        if START_BATTLE == 1: 
            battler = ctx.author.name
            
            if ctx.author.name != LAST_TURN: 
                await ctx.send(trainers[battler].attack(trainers[loser]))
                LAST_TURN = ctx.author.name

            else:
                return await ctx.send('It is not your turn!')

            c1 = 0
            c2 = 0
            for pok in trainers[battler].pokemon_list:
                if pok.ko == 1:
                    c1 += 1
                
                if c1 == len(trainers[battler].pokemon_list):
                    await ctx.send(f'\n\n---------- Congratulations {(trainers[loser].name).upper()} you have defeated {(trainers[battler].name).upper()} in battle! ----------\n\n')
                    LAST_TURN = ''
                    START_BATTLE = 0

            for pok in trainers[loser].pokemon_list:
                if pok.ko == 1:
                    c2 += 1
                
                if c2 == len(trainers[loser].pokemon_list):
                    await ctx.send(f'\n\n---------- Congratulations {(trainers[battler].name).upper()} you have defeated {(trainers[loser].name).upper()} in battle! ----------\n\n')
                    LAST_TURN = ''
                    START_BATTLE = 0
        
    except: 
        return await ctx.send('Please start a battle with another trainer')

@client.command() # Trainer command to switch to a different pokemon in your pokemon list
async def switch_to(ctx, new_poke):
    global LAST_TURN
    battler = ctx.author.name
    
    if ctx.author.name != LAST_TURN: 
        return await ctx.send(trainers[battler].switch_pokemon(new_poke))
    
    else: 
        return await ctx.send('It is not your turn!')


@client.command() # Trainer command to display Trainer summaries (detaults to your summary)
async def status(ctx, *battler):
    try: 
        await ctx.send(trainers[battler[0]].pokemon_status())

    except:
        battler = ctx.author.name
        await ctx.send(trainers[battler].pokemon_status())

@client.command()
async def potion(ctx, poke):
    global LAST_TURN 
    battler = ctx.author.name

    if ctx.author.name != LAST_TURN: 
        await ctx.send(trainers[battler].use_potion(poke))
    
    else: 
        return await ctx.send('It is not your turn!')

# -----------------------------------------------------------------------
# Misc Bot commands


@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Qestion: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['blink_me'])
async def bp(ctx):

    await ctx.send(f'Enjoy: {random.choice(blink_songs)}')

@client.command(aliases=['bae_me'])
async def blink_bae(ctx):

    if ctx.author.name == 'iamsmore':
        await ctx.send('Your bae of the day is Lesly Garza')

    elif ctx.author.name == 'Saph':
        await ctx.send(f'Your bae of the day is {random.choice(girl_names)}')

    else: 
        await ctx.send(f'Your bae of the day is {random.choice(baes)}')



client.run('')




"""

How to Play: 

    Commands: 

        .status
            - Gives you a summary of a Trainer's account
                - Ex: 
                    - .status => Returns summary of your Trainer's account (default)
                    - .status Saph => Returns a summar of Saph's Trainer account

        .battle XXXX
            - Starts a battle with XXXX (where XXXX is a trainer's name)
                - Ex: 
                    - .battle Saph => Enters a battle between you and Saph

        .switch_to XXXX
            - Switches your currently active Pokemon to XXXX (where XXXX is a name from a Pokemon in your Trainer's pokemon list)





"""