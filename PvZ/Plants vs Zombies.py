class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        print("Zombie moves.")
        self.distance-=1

    def take_damage(self, amount):
        self.health-=amount
        print(f"{self.name} has {self.health} Health left.")
        if self.health<=0:
            print(f"{self.name} has died.")

    def attack(self, plant):
        if self.distance>0:
            self.move()
        elif self.damage>0:
            print(f"Chomp! {plant.name} takes {self.damage} Damage.")
            plant.take_damage(self.damage)
        else:
            print("Grrr!")
            print(f"{plant.name} takes 0 damage. What do you expect?")

class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage    

    def attack(self, zombie):
        if self.health>0 and self.damage>0:
            print(f"{zombie.name} takes {self.damage} Damage from {self.name}.")
            zombie.take_damage(self.damage)
        elif self.damage==0:
            print(f"{self.name} flails around.")
            print(f"{zombie.name} takes 0 damage. What do you expect?")


    def take_damage(self, amount):
        self.health-=amount
        print(f"{self.name} has {self.health} Health left.")
        if self.health<=0:
            print(f"{self.name} died.")
zombie1=Zombie("Conehead Zombie",140,12,1)
plant1=Plant("Peashooter", 12, 0)
plant2=Plant("Repeater",13,13)

while True:
    if plant1.health>0:
        zombie1.attack(plant1)
    else:
        zombie1.attack(plant2)
    plant1.attack(zombie1)
    plant2.attack(zombie1)
    if zombie1.health<=0:
        print("Plants win!")
        break
    elif plant1.health+plant2.health<=0:
        print("Zombies win!")
        break