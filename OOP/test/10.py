class Cashier:
    def __init__(self, products):
        self.products = products
    def recommend(self):
        self.products_list = ', '.join(self.products)
        print('We have ' + self.products_list + '.')

cashier = Cashier(['apple', 'banana', 'orange'])
cashier.recommend()