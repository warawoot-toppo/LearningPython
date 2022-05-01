class Book:
    def __init__(self,book_name,book_status = 'available'):
        self.name = book_name
        self.status = book_status
    def borrow_book(self):
        if self.status == 'available':
            print('borrow successfully')
            self.status = 'unavailable'
        elif self.status == 'unavailable':
            print('borrow unsuccessfully') 
    def return_book(self):
        if self.status == 'unavailable':
            print('return successfully')
            self.status = 'available'
        elif self.status == 'available':
            print('return unsuccessfully')    


book1 = Book('toppo')
  
print(book1.status)
book1.borrow_book()
print(book1.status)
book1.return_book()   
print(book1.status)