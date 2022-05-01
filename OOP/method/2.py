class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    def set_color(self, color):
        self.color = color    
car1 = Car('Toyota', 'Camry', 'Black')
print(car1.color)
car1.set_color('Red')
print(car1.color)