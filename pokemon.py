import random

class Pokemon():
    def __init__(self, name, level, type, max_health, current_health, ko):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.ko = ko
        # self.exp = exp


    def lose_health(self, damage):
        self.current_health -= damage

        if self.current_health <= 0:
            return self.knock_out()

        return '{name} now has {health} health!'.format(name=self.name, health = round(self.current_health, 2))

            
    def regaining_health(self):
        if self.ko == 0:
            self.current_health += 10
            return '{name} now has {health} health!'.format(name=self.name, health = self.current_health)

        if self.ko == 1: 
            return '{name} has died, like died forreal forreal'.format(name=self.name)

    def knock_out(self):
        self.ko = 1
        return 'RIP {name} has died!!!'.format(name=self.name)


    def revive(self):
        self.ko = 0
        self.current_health = self.max_health
        print('{name} has been revived! Current health is {health}'.format(name=self.name, health = self.current_health))


    """
    def gain_exp(self):
        self.exp = 0
    """
    
    
    def make_baby(self,mate):
        #at least one pokemon needs to be level 18 to reproduce
        #they need to be same pokemon
        
        if self.name == mate.name and (self.level >= 18 or mate.level >= 18):
            baby = Pokemon(self.name,1,self.type,self.max_health,self.max_health, 0)
            print(f"Congrats, you are gonna be a father to a baby")
            return baby
        else:
            print(f"These pokemon are not compatable")

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
                
        attack_dialogue = '{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name)
        lose_health_dialogue = victim.lose_health(round(self.damage, 2))
        return attack_dialogue + '\n' + lose_health_dialogue 



class Trainer():
    def __init__(self, pokemon_list,  name, potions, currently_active):
        self.pokemon_list = pokemon_list
        self.name = name
        self.potions = potions
        self.currently_active = currently_active

    def use_potion(self):
        if self.potions < 1:
            print('{trainer} is out of potions!'.format(trainer=self.name))
 
        elif self.pokemon_list[self.currently_active].current_health < self.pokemon_list[self.currently_active].max_health:
            self.potions -= 1
            print('{trainer} used potion on {pokemon} ({potions} potions remaining)'.format(trainer=self.name, pokemon=self.pokemon_list[self.currently_active].name, potions=self.potions))
            self.pokemon_list[self.currently_active].regaining_health()

        else: 
            print('{pokemon} is at max health!'.format(pokemon=self.pokemon_list[self.currently_active].name))

    def attack(self, sufferer):
        battle_dialogue = '{self} has decided to battle {sufferer}!'.format(self=self.name, sufferer=sufferer.name)

        if sufferer.pokemon_list[sufferer.currently_active].ko == 1:
            battle_dialogue_dead =  'You cannot attack a dead pokemon. {sufferer} please change your currently active Pokemon'.format(sufferer=sufferer.name)
            return battle_dialogue_dead

        return battle_dialogue + '\n' + self.pokemon_list[self.currently_active].attack(sufferer.pokemon_list[sufferer.currently_active])


    def switch_pokemon(self, new):


        for i in range(len(self.pokemon_list)):
            if self.pokemon_list[i].name == new:
                self.currently_active = i
                return '{self} is switching Pokemon to {new_pokemon}'.format(self=self.name, new_pokemon=self.pokemon_list[i].name)


        return 'Error: You do not own this pokemon'

        
    def pokemon_status(self):
        return_string = '------------------- Trainer {name} Summary ------------------- \n'.format(name=(self.name).upper())

        return_string += '\nPOKEMONS\n'
        for poke in self.pokemon_list:

            health_bar = '----------'
            percent_health = round((poke.current_health/poke.max_health)*10)
            

            if poke.ko == 1:
                return_string += '- {name} [{health}] {current}/{total} HP (DEAD)'.format(name=(poke.name).upper(), current=round(poke.current_health, 2), total=poke.max_health, health=health_bar)

                if self.pokemon_list[self.currently_active].name == poke.name:
                    return_string += ' *currently active*'
                return_string += '\n'

            else:
                health_list = list(health_bar)
                for i in range(percent_health):
                    health_list[i] = "+"

                current_health_bar = "".join(health_list)
            


                return_string += '- {name} [{health}] {current}/{total} HP'.format(name=(poke.name).upper(), current=round(poke.current_health, 2), total=poke.max_health, health=current_health_bar)
                if self.pokemon_list[self.currently_active].name == poke.name:
                    return_string += ' *currently active*'
                return_string += '\n'


        return_string += '\nPotions remaining: {pots}'.format(pots=self.potions)

        return return_string 





#charmander.lose_health(20)
#May.use_potion()
#May.use_potion()
#May.use_potion()
#sputnicc.attack(Saph)





