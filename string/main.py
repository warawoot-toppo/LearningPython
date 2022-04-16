
message = 'a, b, c, d, 2'

# คำสั่งตรวจสอบข้อความว่ามีกี่ตัวอักษร 
result_1 = len(message) 
print(result_1)

# คำสั่งตรวจสอบข้อความย่อยจากข้อความทั้งหมด
result_2 = 'a' in message 
print(result_2)

# คำสั่งตรวจสอบว่าใน message เป็นตัวเลขทั้งหมดหรือไม่
result_3 = message.isdigit() 
print(result_3)

# คำสั่งเปลี่ยนตัวอักษรเล็กให้เป็นอักษรใหญ่ ไม่มีผลกับตัวอักษร Original
result_4 = message.upper()
print(result_4)

# คำสั่งเปลี่ยนข้อความเดิมให้เป็นข้อความอื่น ไม่มีผลกับข้อความ Original
result_5 = message.replace('d', 'rabbit')
print(result_5)

# คำสั่งแปลงข้อความเป็น list   ', ' = ใช้ในการตัดข้อความเป็น list
ABC = message.split(', ')
print(ABC)

# คำสั่งเปลี่ยน list ให้กลายเป็นข้อความโดยมีเครื่องหมายกั้น
new_message =' + '.join(ABC)
print(new_message)


