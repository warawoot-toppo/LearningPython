class Tree:
    def __init__(self, height, width, generrated_money):
        self.height = height
        self.width = width
        self.generrated_money = generrated_money
        print('Height :', self.height, ',Width :', self.width, ',Generated Money :', self.generrated_money)
    def feed_A(self):
        self.generrated_money -= 10
        self.width += 12
        print('Width :', self.width, ',Generated Money :', self.generrated_money) 
    def feed_B(self):
        self.generrated_money -= 8
        self.height += 10
        print('Height :', self.height, ',Generated Money :', self.generrated_money)
    def sell(self):
        self.generrated_money  += (self.width * self.height) * 0.8
        self.width = 0
        self.height = 0
        print('Generated Money :', self.generrated_money)


tree_A = Tree(10, 10, 1000)
tree_A.feed_A()
tree_A.feed_B()
tree_A.sell()