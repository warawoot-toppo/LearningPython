class Tank_1:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def add_ammo(self, ammo):
        if self.ammo + ammo <= 10:
            self.ammo += ammo 

    def fire_ammo(self):
        if self.ammo > 0:
            self.ammo -= 1
