class Pokemon(): 
    def __init__(self, name, level, type, max_health, current_health, ko):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.ko = ko


    def lose_health(self, damage):
        self.current_health -= damage
        print('{name} now has {health} helath!'.format(name=self.name, health = self.current_health))

        if self.current_health <= 0:
            print('Ouch!')
            self.knock_out()
            

    def regaining_health(self):
        if self.ko == 0:
            self.current_health += 10
            print('{name} now has {health} helath!'.format(name=self.name, health = self.current_health))

        if self.ko == 1: 
            print('{name} has fainted, you must revive this Pokemon first'.format(name=self.name))


    def knock_out(self):
        self.ko = 1
        print('{name} has fainted!'.format(name=self.name))


    def revive(self):
        self.ko = 0
        self.current_health = self.max_health
        print('{name} has been revived! Current health is {health}'.format(name=self.name, health = self.current_health))

    def attack(self, victim): 
        if self.type == 'Fire':
            if victim.type == 'Grass': # x2
                self.damage = 2 * self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)

            elif victim.type == 'Water': # x1/2
                self.damage = 0.5 * self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)
            else:
                self.damage = self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)

        if self.type == 'Water':
            if victim.type == 'Fire': # x2
                self.damage = 2 * self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)
            elif victim.type == 'Grass': # x 1/2
                self.damage = 0.5 * self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)
            else:
                self.damage = self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)

        if self.type == 'Grass':
            if victim.type == 'Water': # x2
                self.damage = 2 * self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)
            elif victim.type == 'Fire': # x1/2
                self.damage = 0.5 * self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)
            else:
                self.damage = self.level
                print('{attacker} has attacked {victim}!'.format(attacker=self.name, victim=victim.name))
                victim.lose_health(self.damage)

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
        print('{self} has decided to battle {sufferer}!'.format(self=self.name, sufferer=sufferer.name))
        self.pokemon_list[self.currently_active].attack(sufferer.pokemon_list[sufferer.currently_active])
        #print(self.pokemon_list[self.currently_active].name)
        #print(sufferer.pokemon_list[sufferer.currently_active].name)


    def switch_pokemon(self, new):
        print('{self} is switching Pokemon to {new_pokemon}'.format(self=self.name, new_pokemon=self.pokemon_list[new].name))
        self.currently_active = new
        


charmander = Pokemon('Charmander', 10, 'Fire', 50, 50, 0)
squirtle = Pokemon('Squirtle', 10, 'Water', 50, 50, 0)
bulbasaur = Pokemon('Bulbasaur', 10, 'Grass', 50, 50, 0)
charizard = Pokemon('Charizard', 10, 'Fire', 50, 50, 0)

Ash = Trainer([squirtle, bulbasaur], 'Ash', 3, 0)
May = Trainer([charmander, charizard], 'May', 5, 0)

#charmander.lose_health(20)
#May.use_potion()
#May.use_potion()
#May.use_potion()

Ash.attack(May)
Ash.attack(May)
Ash.attack(May)
Ash.attack(May)
Ash.attack(May)


