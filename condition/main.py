'''การตรวจสอบเงื่อนไข'''


score = 100
if score >= 90: # if ใช้ในการตรวจเงื่อนไขเพื่อ run คำสั่งต่อไป จบด้วยเรื่องหมาย(:)(โคล่อน)
    print('สูง')
elif score >= 80: # elif ใช้ก็ต่อเมื่อ if เป็น False เพื่อ run คำสั่งอีกชุด จบด้วยเรื่องหมาย(:)(โคล่อน)
    print('กลาง')
elif score >= 70:
    print('ต่ำ')
else: # else ใช้ก็ต่อเมื่อ if และ elif เป็น False เพื่อ run คำสั่งชุดสุดท้าย จบด้วยเรื่องหมาย(:)(โคล่อน)
    print('ต่ำมาก')