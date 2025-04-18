class Pet:
    def __init__(self, name):
        self.name = name 
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []


    def eat(self):
        self.hunger = max(0, self.hunger -3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some meat. The rate of hunger decreased whereas happy feelings heightened!")


    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Energy: {self.energy}")

              
    def play(self):
        self.energy = max(0, self.energy -2)
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} is soo playful. Evey time we play his energy decreases but he is overly happy!")


    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = max(0, self.happiness - 1)
        print(f"{self.name} loves learning new tricks: {trick}")


    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} does not know any tricks!")
        else:
            print(f"{self.name} has learnt new tricks: {',' .join(self.tricks)}")


    def get_status(self):
        print("f\n{self.name}'s status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
              
        
      