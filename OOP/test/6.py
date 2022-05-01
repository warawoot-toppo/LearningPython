class ComplexNumber:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def get_value(self):
        print(self.r,'+',str(self.i)+'i')
z = ComplexNumber(2,5)
z.get_value()            