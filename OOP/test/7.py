class Car:
    def __init__(self, brand, model, years, color):
        self.brand = brand
        self.model = model
        self.years = years
        self.color = color
    def new_color(self,color):
        self.color = color
        return self.color

car_A = Car('Honda', 'Civic', '2019', 'Black')
car_A.new_color('Red')
print(car_A.color)