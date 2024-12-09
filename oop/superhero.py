class Superhero():
    def __init__(self, superhero_name, superhero_identity, superhero_power, superhero_archenemy, superhero_transform):
        self.name = superhero_name
        self.identity = superhero_identity
        self.power = superhero_power
        self.enemy = superhero_archenemy
        self.transform = superhero_transform
    
    def introduce(self):
        print(f"My normal name is {self.identity}, but I fight crime under the alias of {self.name}!")
        print(f"I {self.power}, an essential power to save the day.")
        print(f"I have fought many enemies including my arch nemesis, {self.enemy}.")

    def transform(self):
        print(f"{self.identity} {self.transform} and became {self.name}!")