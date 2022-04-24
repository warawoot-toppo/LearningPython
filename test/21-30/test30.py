'''
เขียนโปรแกรมหาจำนวนเฉพาะ 100 ตัวแรก และพิมพ์ออกมา
'''
a = 1
count_prime = 0

while count_prime < 100:
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count = count + 1
    if count == 2:
        print(a)
        count_prime = count_prime + 1
    a = a + 1
    

