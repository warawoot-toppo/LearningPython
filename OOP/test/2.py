class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def aging(self,years):
        print('อายุปัจจุบันคือ %s' %self.age)
        self.age += years
        print('หลังจากผ่านไป %s ปี เขาก็มีอายุ %s ปี' %(years,self.age))

human1 = Human('top', 29)
human1.aging(6)