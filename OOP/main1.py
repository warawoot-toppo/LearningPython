import Class_Object_test as t
import tkinter as tk

window = tk.Tk()
window.title('ผามม')
window.minsize(400, 400)


first_tank = t.Tank_1('toppo', 3)
first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)



first_tank.add_ammo(5)
print(first_tank.ammo)
