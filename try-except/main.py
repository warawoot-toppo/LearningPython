try: # try = เอาไว้ครอบข้อมูลที่มีความเสี่ยง error สูงใช้แก้ error ให้ทำงานได้ปกติ
    x = int(input('X = ')) # input() = คำสั่งเอาไว้ใส่ข้อมูลหน้า terminal
    y = int(input('Y = '))
    if x == 0:
        raise Exception() # raise Exception() = คำสั่งแจ้งเตือน error ส่งไปที่ except
    z = x / y
    print(z)

except: # except = ใช้ในการแสดงผลเมื่อเกิด error ขึ้น
    print('unknow')

print('toppo')