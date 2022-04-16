import tkinter as tk # tkinter=library ของ python

def set_message(): #def=คำสั่งในการสร้างฟังก์ชั่น, set_message=ชื่อฟังก์ชั่น
    text = text_input.get() #text=ตัวแปร, ext_input=ชื่อตัวแปร, get=เป็นคำสั่งที่นำข้อความที่กรอกเข้าไปนำมาใช้งานได้
    title_label.configure(text=text) #title_label=ตัวแปร, configure=คำสั่งในการเปลี่ยนค่า parameter


window = tk.Tk() #window=ตัวแปล, tk=tkinter, Tk=คำสั่งใน tkinter ใช้ในการสร้างแอพ
window.title('justPython') #title=คำสั่งในการตั้งชื่อแอพ
window.minsize(400,400) #minsize=คำสั่งกำหนดขนาดแอพ(width*height)

title_label = tk.Label(master=window, text='toppoV123') #title_label=ตัวแปล, #Label=คำสั่งใน tkinter ใช้ในการสร้างข้อความ
#master=คือ parameter เป็นตัวระบุว่าให้นำ Label ไปไว้ที่ไหน
#text=คือ parameter เป็นตัวระบุว่าให้ข้อความเขียนว่าอะไร
title_label.pack() #pack=คำสั่งแสดง title_label ขึ้นในแอพ

text_input = tk.Entry(master=window) #text_input=ตัวแปร, Entry=คำสั่งใน tkinter ใช้ในการสร้างช่องกรอกข้อความ
#master=คือ parameter เป็นตัวระบุว่าให้นำ Entry ไปไว้ที่ไหน
text_input.pack() #pack=คำสั่งแสดง text_input ขึ้นในแอพ

ok_button = tk.Button(master=window, text='ok', command=set_message)#ok_button=ตัวแปร
#Button=คำสั่งใน tkinter ใช้ในการสร้างปุ่มกด, text=คือ parameter เป็นตัวระบุว่าให้ข้อความเขียนว่าอะไร
#text=คือ parameter เป็นตัวระบุว่าให้ข้อความเขียนว่าอะไร
#command=คำสั่งเมื่อเวลากดปุมจะให้แสดงคำสั่งอะไรต่อ, set_message=ชื่อฟังก์ชั่น
ok_button.pack()#pack=คำสั่งแสดง ok_button ขึ้นในแอพ

window.mainloop() #mainloop=คำสั่งเรียกใช้แอพ