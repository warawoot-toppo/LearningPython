from lib2to3.pgen2 import driver


class Driver:
    def __init__(self, HP, generrated_money):
        self.HP = HP
        self.generrated_money = generrated_money
        print('HP = %s, Generated Money = %s' %(self.HP, self.generrated_money)) 
    def drive(self):
        self.HP = max(0, self.HP - 10)
        self.generrated_money += 10
        if self.HP == 0:
            print('เสียชีวิตเนื่องจากหักโหม')
        print('HP = %s, Generated Money = %s' %(self.HP, self.generrated_money)) 
    def care(self):
        self.HP += 10
        self.generrated_money -= 10
        if self.generrated_money < 0:
            print('มีหนี้สินเนื่องจากไม่ทำงาน')
        print('HP = %s, Generated Money = %s' %(self.HP, self.generrated_money)) 

driver_a = Driver(20, 20)
driver_a.care()
driver_a.drive()
driver_a.drive()
driver_a.drive()
driver_a.care()
driver_a.care()
driver_a.care()
driver_a.care()
driver_a.care()