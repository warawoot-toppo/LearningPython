class Warrior:
    def __init__(self, HP, ATK, DEF):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
    def Training(self):
        self.HP += 5
        self.ATK += 10
        self.DEF += 5 

warrior1 = Warrior(100, 45, 25)
warrior1.Training()
print(warrior1.HP)
print(warrior1.ATK)
print(warrior1.DEF)