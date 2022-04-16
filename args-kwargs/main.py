def average(*scores): # * args = รับ parameter แบบไม่ตั้งชื่อมากี่ตัวก็ได้
    print(scores)
    sum_score = sum(scores)
    average_score = sum_score / len(scores)
    return average_score

#print(average(75, 50, 65))

def check_passed(**scores): # ** kwargs = การรับ parameter แบบตั้งชื่อมากี่ตัวก็ได้
    math = scores.get('math')
    physics = scores.get('physics')
    english = scores.get('english')
    if math is not None and math >= 50:
        print('สอบผ่านคณิต')
    if physics is not None and physics >= 50:
        print('สอบผ่านฟิสิกส์')
    if english is not None and english >= 50:
        print('สอบผ่านอังกฤษ')

check_passed(math=80, physics=35, english=70)    
