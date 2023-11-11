class Animal:
    def __init__(self, species):
        self.species = species

    def reproduction(self):
        pass

class Mammal(Animal):
    def __init__(self, species, colour):
        super().__init__(species)
        self.colour = colour

    def reproduction(self):
        print(f"The {self.colour} {self.species} gives birth to babies.")

class Fish(Animal):
    def __init__(self, species, colour):
        super().__init__(species)
        self.colour = colour

    def reproduction(self):
        print(f"The {self.colour} {self.species} lays eggs in the water.")

class Bird(Animal):
    def __init__(self, species, colour):
        super().__init__(species)
        self.colour = colour

    def reproduction(self):
        print(f"The {self.colour} {self.species} lays eggs in its nest.")

lion = Mammal("Lion", "golden")
lion.reproduction()

tuna = Fish("Tuna", "silver")
tuna.reproduction()

seagull = Bird("Seagull", "white")
seagull.reproduction()
