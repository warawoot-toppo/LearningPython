from re import L
from tkinter import W


class Box:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
    def display_volume(self):
        print('Volume: ', self.width * self.length * self.height)
    
    def display_dimensions(self):
        print('Dimensions: ',self.width, 'x', self.length, 'x', self.height)

b1 = 2
list_of_oj = [None] * b1

for i in range(b1):
    W = float(input('Enter width: '))
    l = float(input('Enter length: '))
    h = float(input('Enter height: '))
    list_of_oj[i] = Box(W, l, h)

for i in range(b1):
    list_of_oj[i].display_dimensions()
    list_of_oj[i].display_volume()
