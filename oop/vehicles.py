class Vehicle():
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def move(self):
        print(f"The {self.name} has started to move!")

    def turn(self):
        print(f"The {self.name} has changed direction!")

class Bicycle(Vehicle):
    def __init__(self, name, size, gears):
        self.gears = gears
        super().__init__(name, size)
    
    def wheelie(self):
        print(f"The {self.name} raised its front wheel and did a wheelie!")

class Plane(Vehicle):
    def __init__(self, name, size, wingspan):
        self.wingspan = wingspan
        super().__init__(name, size)
    
    def fly(self):
        print(f"The {self.name} is flying to its next destination!")