import datetime as dt # datetime = module สำหรับวัน/เวลา
date1 = dt.datetime.now() # dt.datetime.now() function แสดงเวลาปัจจุบัน
print(date1)

date2= dt.datetime(year=2020, month=2, day=14, hour=13, minute=30) # dt.datetime() = function แสดงวันเวลาที่กำหนด
date2_1 = dt.datetime(year=2020, month=2, day=20, hour=16)
days1 = date2_1 - date2
print(days1)

print(date2.strftime('%A %d, %B %Y')) # date2.strftime = function แสดงวันเวลาแบบมีชื่อเรียก

days = dt.timedelta(days=25) # dt.timedelta = function การสร้างระยะเวลาเพื่อนำมา'เพิ่ม/ลบ'กับเวลาหลัก
date3 = date2 + days
print(date3)