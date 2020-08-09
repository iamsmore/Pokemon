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
            print('Ouch!')
            self.knock_out()

        return '{name} now has {health} health!'.format(name=self.name, health = self.current_health)

            
    def regaining_health(self):
        if self.ko == 0:
            self.current_health += 10
            print('{name} now has {health} health!'.format(name=self.name, health = self.current_health))

        if self.ko == 1: 
            print('{name} has fainted, you must revive this Pokemon first'.format(name=self.name))

    def knock_out(self):
        self.ko = 1
        print('{name} has fainted!'.format(name=self.name))


    def revive(self):
        self.ko = 0
        self.current_health = self.max_health
        print('{name} has been revived! Current health is {health}'.format(name=self.name, health = self.current_health))


    #def gain_exp(self):
    #    self.exp = 

    
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
        #self.pokemon_list[self.currently_active].attack(sufferer.pokemon_list[sufferer.currently_active])

        return battle_dialogue + '\n' + self.pokemon_list[self.currently_active].attack(sufferer.pokemon_list[sufferer.currently_active])
        #print(self.pokemon_list[self.currently_active].name)
        #print(sufferer.pokemon_list[sufferer.currently_active].name)

    def switch_pokemon(self, new):
        print('{self} is switching Pokemon to {new_pokemon}'.format(self=self.name, new_pokemon=self.pokemon_list[new].name))
        self.currently_active = new
        


#charmander.lose_health(20)
#May.use_potion()
#May.use_potion()
#May.use_potion()
#sputnicc.attack(Saph)





