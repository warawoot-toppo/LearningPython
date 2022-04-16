import tkinter as tk

def show_output():
    
    '''number=ตัวแปรเก็บค่าตัวเลข, int=คำสั่งเปลี่ยนข้อมูลเป็นเลขจำนวนเต็ม, numbet_input=ตัวแปร, 
    get=คำสั่งนำข้อความที่ใส่มาใช้งาน(คืนค่าเป็นข้อความเสมอ)'''

    try:
        number = int(number_input.get())
        if number == 0:
            raise Exception()


    except:
        output_label.configure(text='ไม่สามารถคำนวนได้')
        return

    output = ''
    for i in range(1, 13):
        output +=str(number) + ' x ' + str(i) + ' = ' + str(number * i) + '\n'
    output_label.configure(text=output)

window = tk.Tk()
window.title('justpython')
window.minsize(400,400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack(pady=20)

number_input = tk.Entry(master=window,width=25)
number_input.pack()

go_button = tk.Button(master=window, text='ได้แก่', command=show_output, width=15, height=2)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()