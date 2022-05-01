class Dog:
    def __init__(self, breed, color, height, weight):
        self.breed = breed
        self.color = color
        self.height = height
        self.weight = weight
    def growth(self):
        height_up = self.height * 1.1 
        weight_up = self.weight * 1.1 
        return height_up, weight_up

dog_A = Dog('Jack Russell Terrier', 'white', 30, 7)
print(dog_A.growth())