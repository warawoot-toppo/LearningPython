import math # math = module เกี่ยวกับการคำนวนทางคณิตศาสตร์

a = math.floor(32.5) # math.floor = คำสั่งสำหรับปัดเศษลง
b = math.ceil(32.5) # math.ceil = คำสั่งสำหรับปัดเศษขึ้น

print(a)
print(b)

A = 6
B = 8
C = math.sqrt(A ** 2 + B ** 2) # math.sqrt = คำสั่งเรียกใช้สแควรูท
print(C)

scors = [10, 20, 40, 80, 100]

min_scor = min(scors) # min = คำสั่งหาค่าที่น้อยสุด

max_scor = max(scors) # max = คำสั่งหาค่าที่มากสุด

print(min_scor)
print(max_scor)