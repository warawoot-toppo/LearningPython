#  class = คำสั่งใช้ในการสร้าง object 
class Tank:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

# คำสั่งในการเรียกใช้ object จาก class 
first_tank = Tank('toppo', 3)

# คำสั่งแก้ไขชื่อ object
first_tank.name = 'toppo_0'

# คำสั่งแก้ไขตัวเลข object
first_tank.ammo += 2


print(first_tank.name)     

second_tank = Tank('toppo_1', 6)
print(second_tank.name)
