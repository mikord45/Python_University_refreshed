class Animal:
    def __init__(self, species):
        self.species = species

    def describe(self):
        print(f"Jestem zwierzęciem gatunku {self.species}.")


class Bird(Animal):
    def __init__(self, species, wingspan, plumage_color):
        super().__init__(species)
        self.wingspan = wingspan
        self.plumage_color = plumage_color

    def sing(self):
        print(f"{self.species} śpiewa piękną pieśń.")

    def fly(self):
        print(f"{self.species} fruwa majestatycznie.")

    def information_about_bird(self):
        print(f"Ptak: {self.species}, Rozpiętość skrzydeł: {self.wingspan} cm, Kolor upierzenia: {self.plumage_color}")


my_bird = Bird("Wróbel", 20, "Brązowy")
my_bird.describe()
my_bird.sing()
my_bird.fly()
my_bird.information_about_bird()
print("=====")


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def describe(self):
        print(f"Name: {self.name}, Health: {self.health}")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} took {damage} damage. Remaining health: {self.health}")


class Warrior(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self):
        print(f"{self.name} attacks with strength {self.strength}")

    def defend(self):
        print(f"{self.name} is defending.")


my_warrior = Warrior("Conan", 100, 50)

my_warrior.describe()

my_warrior.attack()
my_warrior.defend()

my_warrior.take_damage(30)
my_warrior.take_damage(80)
