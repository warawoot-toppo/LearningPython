class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print('My name is', self.name + '.','I\'m', self.age, 'yeare old') 

people1 = People('John',23)
people1.introduce()