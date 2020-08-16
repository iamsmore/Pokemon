import random

class Pokemon():
    def __init__(self, name, level, type, max_health, current_health, ko, exp):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.ko = ko
        self.exp = exp


    def lose_health(self, damage):
        self.current_health -= damage
        self.level_up(damage)

        if self.current_health <= 0:
            return self.knock_out(damage)

        hit_string = '\nOUCH! {dam} damage was dealt to {name}'.format(name=self.name, dam=damage)
        hit_string += '\n{name} now has {health}/{max_health} HP!'.format(name=(self.name).upper(), health = round(self.current_health, 2), max_health=self.max_health)
        return hit_string
            
    def regaining_health(self):
        POTION_STR = 10

        if self.ko == 0: 

            if self.current_health + POTION_STR > self.max_health:
                self.current_health = self.max_health

            else:
                self.current_health += POTION_STR

            regaining_health_string =  '\n{name} has been healed and now has {health} health!'.format(name=(self.name).upper(), health = round(self.current_health, 2))
            return regaining_health_string
            
        if self.ko == 1:
            self.current_health = POTION_STR
            regaining_health_string = '\n{name} has been REVIVED and now has {health} health!'.format(name=(self.name).upper(), health = round(self.current_health, 2))
            self.ko = 0
            return regaining_health_string

    def knock_out(self, damage):
        self.ko = 1
        ko_string = '\nOUCH! {dam} damage was dealt to {name}'.format(name=self.name, dam=damage)
        ko_string += '\nRIP {name} has died!!!'.format(name=self.name)
        return ko_string


    def revive(self):
        self.ko = 0
        self.current_health = self.max_health
        print('{name} has been revived! Current health is {health}'.format(name=self.name, health = self.current_health))
 
    
    def make_baby(self,mate):
        #at least one pokemon needs to be level 18 to reproduce
        #they need to be same pokemon
        
        if self.name == mate.name and (self.level >= 18 or mate.level >= 18):
            baby = Pokemon(self.name,1,self.type,self.max_health,self.max_health, 0)
            print(f"Congrats, you are gonna be a gender-neutral gaurdian to a baby")
            return baby
        else:
            print(f"These pokemon are not compatable")
                # implement pokemon size comparison to determine coitus compatibility?

    def level_up(self, damage):
        # keeps track of pokemon level based on amount of accumulated experience
        self.exp += round(damage * 3)
        print(self)

        min_level = 1
        max_level = 100

        possible_levels = list(range(min_level, max_level + 1))
        experience_levels = []

        for level in possible_levels:
            if level <= 10:
                experience_levels.append(level * 200)
            elif level <= 20:
                experience_levels.append(level * 2 * 200)
            elif level <= 30:
                experience_levels.append(level * 3 * 200)
            else:
                experience_levels.append(level * 4 * 200)

        if self.exp < 80000:
            level_position = [i for i,x in enumerate(experience_levels) if x <= self.exp < experience_levels[i + 1]]
        else:
            level_position = [99]

        if len(level_position) == 0:
            self.level = 1
        else:
            self.level = possible_levels[level_position[0]]
        
        return self.exp

        # check level. if level changed, announce to trainer
        # if level changes to 20, or 30, call evolution method 

        # change pokemon health as level up
        

    def evolution(self):
        #check if there is available evolution
        
        #every pokemon should have evolution list?
        return     
            
    def attack(self, victim): 

        if self.type == 'Fire':
            if victim.type == 'Grass': # x2
                self.damage = 2 * (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)

            elif victim.type == 'Water': # x1/2
                self.damage = 0.5 * (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)
            else:
                self.damage = (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)

        if self.type == 'Water':
            if victim.type == 'Fire': # x2
                self.damage = 2 * (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)
            elif victim.type == 'Grass': # x 1/2
                self.damage = 0.5 * (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)
            else:
                self.damage = (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)

        if self.type == 'Grass':
            if victim.type == 'Water': # x2
                self.damage = 2 * (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)

            elif victim.type == 'Fire': # x1/2
                self.damage = 0.5 * (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)
            else:
                self.damage = (victim.max_health / 5) * round(1 + random.randrange(-40,40,1)/100, 2)
                
        lose_health_string = victim.lose_health(round(self.damage, 2))

        return lose_health_string



class Trainer():
    def __init__(self, pokemon_list,  name, potions, currently_active):
        self.pokemon_list = pokemon_list
        self.name = name
        self.potions = potions
        self.currently_active = currently_active

    def use_potion(self, poke):

        return_string = ''

        if self.potions < 1:
            return_string += '{trainer} is out of potions!'.format(trainer=(self.name).upper())
            return return_string
 

        for i in range(len(self.pokemon_list)): # checkint to see if pokemon exists in trainer's pokemon list
            if self.pokemon_list[i].name == poke:
                if self.pokemon_list[i].current_health < self.pokemon_list[i].max_health: # if the leath is less than max health.. use potion
                    self.potions -= 1 
                    regain_health_string = self.pokemon_list[i].regaining_health()

                    return_string += regain_health_string
                    return return_string
                
                else: # if pokemon is already at max health, dont' use potion
                    return_string += '\n{pokemon} is at max health!'.format(pokemon=self.pokemon_list[i].name)
                    return return_string

        else: # pokemon not in list
            return_string += 'Error, {pokemon} is not in your Pokemon list!'.format(pokemon=poke)
            return return_string
        
        


    def attack(self, sufferer):
        return_string = ''

        if self.name == sufferer.name:
            return_string += 'You cannot attack yourself!'.format(self=self.name)
            return return_string


        # Checking that Trainer Pokemons are ready for battle
        if self.pokemon_list[self.currently_active].ko == 1:
            return_string += 'You cannot go into battle with a dead pokemon. {self} please chane your currently active Pokemon'.format(self=self.name)
            return return_string

        if sufferer.pokemon_list[sufferer.currently_active].ko == 1:
            return_string +=  'You cannot attack a dead pokemon. {sufferer} please change your currently active Pokemon'.format(sufferer=sufferer.name)
            return return_string

        # Intro Battle String
        #return_string += '\n{self} has decided to battle {sufferer}!'.format(self=(self.name).upper(), sufferer=(sufferer.name).upper())
        return_string += '\n{attacker} has attacked {victim}!'.format(attacker=(self.pokemon_list[self.currently_active].name).upper(), victim=(sufferer.pokemon_list[sufferer.currently_active].name).upper())

        battle_event_string = self.pokemon_list[self.currently_active].attack(sufferer.pokemon_list[sufferer.currently_active])
        return_string += battle_event_string

        return return_string


    def switch_pokemon(self, new):

        for i in range(len(self.pokemon_list)):
            if self.pokemon_list[i].name == new:
                self.currently_active = i
                return '{self} is switching Pokemon to {new_pokemon}'.format(self=self.name, new_pokemon=self.pokemon_list[i].name)

        return 'Error: You do not own this pokemon'

        
    def pokemon_status(self):
        return_string = '------------------- Trainer {name} Summary ------------------- \n'.format(name=(self.name).upper())
        return_string += '\n-------------------POKEMONS-------------------\n'

        for poke in self.pokemon_list:
            health_bar = '----------'
            percent_health = round((poke.current_health/poke.max_health)*10)
            
            return_string += '\n- {name} '.format(name=((poke.name).upper()))
            if self.pokemon_list[self.currently_active].name == poke.name:
                return_string += ' *(currently active)*'
            
            if poke.ko == 1: # Health for dead pokemon
                return_string += '\n--- Health [{health}] 0/{total} HP (DEAD)'.format(total=poke.max_health, health=health_bar)

            else: # Health for alive pokemon
                health_list = list(health_bar)

                for i in range(percent_health):
                    health_list[i] = "+"

                current_health_bar = "".join(health_list)
                return_string += '\n--- Health [{health}] {current}/{total} HP'.format(current=round(poke.current_health, 2), total=poke.max_health, health=current_health_bar)

            return_string += '\n--- Type: {poke_type}'.format(poke_type=poke.type) # Type
            return_string += '\n--- Level: {poke_lvl}'.format(poke_lvl=poke.level) # Level
            return_string += '\n--- Total XP: {ex}'.format(ex=poke.exp)# XP til level up
            return_string += '\n'

        return_string += '\n\n------------------- Items -------------------\n'
        
        return_string += 'Poke Coins: 0\n' # Coins
        return_string += '\n---Potions remaining: {pots}'.format(pots=self.potions) # Potions
        return_string += '\n---Pokeballs remaining: 0' # Pokeballs
        return_string += '\n\n------------------- Trainer {name} Summary ------------------- \n'.format(name=(self.name).upper())
        
        return return_string
