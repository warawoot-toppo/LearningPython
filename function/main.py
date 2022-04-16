def get_box_area(width,length,height):# def=สร้างฟั่งชั่น , พารามิเตอร์=ดึงข้อมูลภายนอกมาคำนวนในฟังชั่น
    if width < 0 or length < 0 or height < 0:
        return 'บักปอบมึง'
    box_area = width * length * height
    return box_area #return=คืนค่ากลับไปให้ตำแหน่งที่เรียกใช้ฟังชั่น

b1 = get_box_area(4,4,2)
b2 = get_box_area(width=1,length=1,height=1)
print(b1)