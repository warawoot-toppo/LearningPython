class Piont:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'Current position : ({self.x}, {self.y})')
    def move_up(self, d):
        self.y += d
        print(f'Current position : ({self.x}, {self.y})')
    def move_down(self, d):
        self.y -= d
        print(f'Current position : ({self.x}, {self.y})')
    def move_left(self, d):
        self.x -= d
        print(f'Current position : ({self.x}, {self.y})')             
    def move_right(self, d):
        self.x += d
        print(f'Current position : ({self.x}, {self.y})')
A =Piont(0,0)
A.move_up(20)
A.move_left(23)
A.move_down(65)
A.move_right(50)

