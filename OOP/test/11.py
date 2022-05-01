class Warrior:
    def __init__(self, power, defense, HP):
        self.power = power
        self.defense = defense
        self.HP = HP
    def attack(self, enemy):
        if enemy.HP > 0 and self.HP > 0:
            enemy.HP = max(0, enemy.HP - max(0, self.power - enemy.defense))
        if enemy.HP == 0:
            print('Enemy died')
                



warrior_A = Warrior(20, 10, 100)
warrior_B = Warrior(20,15,100)
print(warrior_A.HP)
print(warrior_B.HP)
warrior_A.attack(warrior_B)
warrior_B.attack(warrior_A)
print(warrior_A.HP)
print(warrior_B.HP)