quests = ['ปลูกต้นมะม่วง', 'ล้วงปลาไหล', 'ไล่ศัตรูพืช']

# คำสั่งตรวจสอบว่ามีข้อมูลนี้อยู่ใน list หรือเปล่า
if 'ไล่ศัตรูพืช' in quests:
    print('ท่านเข้าเมืองได้')

# เงื่อนไขในการตรวจสอบ list ที่ไม่เกิน 5
max_quests = 5
if len(quests) < max_quests: # len = คำสั่งนับจำนวนข้อมูลที่อยูใน list
    quests.append('จับปลาดุก')
    quests.append('จับปลาดุก')
    quests.append('จับปลาดุก')
    quests.append('จับปลาดุก')
    print(quests)

elif len(quests) > max_quests:
    print('123213')
    
 
    

# คำสั่งเรียง list ใหม่โดยเรียงจากบนลงล่าง
for quest in quests:
    print(quest)

# คำสั่งเรียง list ใหม่โดยเรียงจากบนลงล่างและมีลำดับของ list
for i in range(len(quests)):
    print(str(i + 1) + '. ' + quests[i])