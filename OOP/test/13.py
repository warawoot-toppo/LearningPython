class Businessman:
    def __init__(self, HP, money, happiness):
        self.HP = HP
        self.money = money
        self.happiness = happiness
        print(f'HP : {self.HP}, money : {self.money}, happiness : {self.happiness}')
    def work(self):
        self.HP = max(0,self.HP - 10)
        self.money += 20
        self.happiness += 10
        if self.HP <= 0:
            print('เสียชีวิตอย่างมีความสุข')
        print(f'HP : {self.HP}, money : {self.money}, happiness : {self.happiness}')
    def sleep(self):
        self.HP += 20
        self.money -= 10
        self.happiness += 10
        print(f'HP : {self.HP}, money : {self.money}, happiness : {self.happiness}')
    def play(self):
        self.HP = max(0,self.HP - 10)
        self.money -= 10
        self.happiness += 20
        if self.HP <= 0:
            print('เสียชีวิตอย่างมีความสุข')
        print(f'HP : {self.HP}, money : {self.money}, happiness : {self.happiness}')


John = Businessman(100, 100, 100)
John.work()
John.play()
John.work()
John.play()
John.work()
John.play()
John.work()
John.play()
John.work()
John.play()
