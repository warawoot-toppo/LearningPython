import math

def pretty_number(function): # function สำหรับปรับแต่ง function อื่น
    def new_function(*args, **kwargs):
        number = function(*args, **kwargs)
        return '{:.2f}'.format(number) # '{:.2f}' = สัญลักษน์พิเศษสามารถใช้ตัวเลขนำมาจัด format ในข้อความได้
    return new_function


@pretty_number
def circle_area(radius): # function ในการคำนวนวงกลม
    return math.pi * (radius ** 2)

@pretty_number
def ellipse_area(width, height): # function ในการคำนวนวงรี
    return math.pi / 4 * width * height


print(circle_area(5))
print(ellipse_area(10, 5))