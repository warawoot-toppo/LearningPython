class warrior:
    def __init__(self, HP, ATK, DEF):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

warrior1 = warrior(100, 45, 25)
warrior2 = warrior(120, 50, 50)
print(warrior1.HP)
print(warrior1.ATK)
print(warrior1.DEF)
print()
print(warrior2.HP)
print(warrior2.ATK)
print(warrior2.DEF)
