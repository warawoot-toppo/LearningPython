for i in range(1, 7): #for=ใช้ในการสร้าง loop , i=ตัวแปร , in=เชื่อมตัวแปรกับข้อมูล , range(เรนช์)=สร้างลำดับข้อมูลแบบตัวเลข
    if i % 3 == 0:
        continue # continue=เมื่อเข้าเงื่อนไขจะข้ามลำดับนั้นไป , break=เมื่อเข้าเงื่อนไขจะหยุดการทำงาน
    print(i)