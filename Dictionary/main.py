# คำสั่งที่ใช้ในการเก็บข้อมูลแบบไม่เรียงกัน สามารถแก้ไขข้อมูลได้ {} = Dictionary
book = {'name': 'c++', 'price': 309, 'page': 414}

# คำสั่งแก้ไขข้อมูลใน dictionary
book['page'] = 500

# คำสั่งเพิ่มข้อมูลใน dictionary
book['place'] = 'TU Rangsit'

# คำสั่งลบข้อมูลใน dictionary
book.pop('price')


print(book)
