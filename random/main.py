import random # random = module เกี่ยวกับการสู่ม

damage = random.randint(50, 60) # ramdom.randint = function การสุ่มเลขจำนวนเต็ม
percent = random.uniform(0, 100) # random.uniform = function การสุ่มเลขทศนิยม

if percent < 40:
    damage = damage * 2

print(damage)

moneys = [0, 20, 100, 1000]
money = random.choice(moneys) # random.choice = function การสุ่มข้อมูลใน list
print(money)

money_ = [0, 20, 100, 1000]
random.shuffle(money_) # random.shuffle = function การสลับตำแหน่งข้อมูลใน list
print(money_)