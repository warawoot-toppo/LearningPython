file = open('group_scores.txt') # open = คำสั่งเปิด file 'Text' นำมาใช้งาน
file1 = open('main1.txt')

 # file.read() = คำสั่งแสดงข้อมูลที่อยู่ใน .txt

pass_count = 0

for score in file1:
    score_int = int(score)
    if score_int >= 60:
        pass_count += 1

print(score_int)

pass_count1 = 0

for group_score in file:
    group_scores_list = group_score.split(' ') # split = เปลี่ยนข้อมูลเป็น list
    for score1 in group_scores_list:
        score_int1 = int(score1)
        if score_int1 >= 60:
            pass_count1 += 1

print('Student passed = ' + str(pass_count1))       



