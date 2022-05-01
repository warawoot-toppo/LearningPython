class USDTHB:
    def __init__(self,amount, currency):
        self.amount = amount
        self.currency = currency
    def to_THB(self):
        if self.currency == 'USD': 
            self.amount *= 30
            self.currency = 'THB'
        return self.amount 
    def to_USD(self):
        if self.currency == 'THB':
            self.amount /= 30
            self.currency = 'USD'
        return self.amount 

money = USDTHB(30000, 'USD')
print(money.amount, money.currency)
money.to_THB()
print(money.amount, money.currency)
money.to_USD()
print(money.amount, money.currency)
money.to_USD()
print(money.amount, money.currency)


