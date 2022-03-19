


from random import randint




class Trooper:
    game_name = "Star Wars Duel"
    everyone = []
    def __init__(self , name, attack):
        self.name = name
        self.weapon = "Blaster"
        self.attack = attack
        self.health = 100
        Trooper.everyone.append(self)

    def fight(self,foe): 
        rand_attack = randint(0,self.attack)
        foe.health -= rand_attack
        if(foe.health > 0):
            print(f"{self.name} dameges {foe.name} with a {self.weapon} by {rand_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} obliterated {foe.name} with an attack of {rand_attack} using their {self.weapon}")
        return self


    def heal(self):
        rand_health = randint(1,10)
        future_health = self.health + rand_health
        if Trooper.can_heal(future_health):
            self.health += rand_health
            print(f"{self.name} healed by {rand_health} | Current Health: {self.health}")
        else:
            self.health = 100
            print(f"{self.name} health can't go above 100 | Current Health: {self.health}")

        return self

    @staticmethod
    def can_heal(future_health):
        if future_health > 100:
            return False
        else:
            return True

    @classmethod
    def all_fighters(cls):
        print("Fighters:")
        for fighter in Trooper.everyone:
            print(fighter.name)
            


rex = Trooper("Rex",50)
cody = Trooper("Cody",12)
helmetTrooper = Trooper("Helmet" ,30)

print(f"Welcome to {Trooper.game_name}")
print(f"{rex.name} vs {cody.name}")
print(f"{rex.name}: Attack - {rex.attack} | Health: {rex.health}")
print(f"{cody.name}: Attack - {cody.attack} | Health: {cody.health}") 

rex.fight(cody)
cody.fight(rex)
cody.fight(rex)
cody.fight(rex)
rex.heal()
Trooper.all_fighters()

class Jedi(Trooper):
    def __init__(self, name, attack):
        super().__init__(name, attack)
        self.health =200
        self.weapon = "Light Saber"
        self.force_push_attack = 50
        self.trooper = Trooper("Finn" , 25)

    def force_push(self,foe):
        foe.health -= self.force_push_attack
        if (foe.health > 0):
            print(f"{self.name} dameges {foe.name} with a force push by {self.force_push_attack}")
            print(f"{foe.name} Health: {foe.health}")
        else:
            print(f"{self.name} Obliterated {foe.name} with a force push")

    def heal(self):
        rand_health = randint(1,20)
        future_health = self.health + rand_health
        if Jedi.can_heal(future_health):
            self.health += future_health
            print(f"{self.name} healed by {rand_health} | current health: {self.health}")
        else:
            self.health = 200
            print(f"{self.name} health can't go above 200 | current health{self.health}")

        return self

    @staticmethod
    def can_heal(future_health):
        if (future_health > 200):
            return False
        else:
            return True


obi = Jedi("Obi Wan",75)
yoda = Jedi("Yoda",100)
print(obi.name)
print(obi.health)
print(yoda.name)
print(yoda.trooper.name)
yoda.force_push(obi)
yoda.force_push(rex)
yoda.force_push(rex)
obi.heal()
