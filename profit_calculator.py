from tkinter import *                     #import module ที่ต้องใช้
from tkinter import messagebox

profit = 0                #นิยามตัวแปรสำหรับเก็บค่ากำไร เปอร์เซ็น และผลลัพธ์จากการคำนวณ
percent = 0
result = ''


def calculate():            #นิยามฟังก์ชันที่จะคำนวณกำไร-ขาดทุน
    try:                    #ใช้คำสั่ง try-exception เพื่อตรวจจับข้อผิดพลาด กรณีผู้ใช้กรอกข้อมูลไม่ถูกต้อง
        profit = float(income_input.get()) - float(cost_input.get())
        percent = profit / float(cost_input.get()) * 100
        profit_d = round(profit, 2)
        percent_d = round(percent, 2)
        
        if profit >= 0:                                      #ตรวจสอบว่าได้กำไรหรือขาดทุน
            result = "ได้กำไร "+ str(abs(profit_d)) +" บาท \nคิดเป็น "+ str(abs(percent_d)) +" %"
            result_output.config(text=result)
        elif profit < 0:
            result = 'ขาดทุน '+str(abs(profit_d))+" บาท \nคิดเป็น "+ str(abs(percent_d)) + " %" 
            result_output.config(text=result)
    except:
        messagebox.showerror("Error", "ข้อมูลไม่ถูกต้อง")
def reset():
    print('Reset')


win = Tk()                                      #สร้างหน้าต่างโปรแกรม
win.title('Profit and Loss Calculator')         #ใส่ Title ของโปรแกรม
win.geometry('800x600')                 #กำหนดขนาดหน้าต่าง
win.config(bg='#B0E0E6')                #กำหนดสีพื้นหลัง
win.option_add('*Label.background', '#B0E0E6')

label_head1 = Label(text="โปรแกรมคำนวณกำไร-ขาดทุน", font='tahoma 16 bold')
label_head1.pack(pady=5)

label_income = Label(text='รายได้' , font='tahoma 14 ')
label_income.pack(pady=5)

income_input = Entry()              #สร้างช่องรับค่ารายได้
income_input.pack(pady=5)

label_cost = Label(text='ต้นทุน', font='tahoma 14')           
label_cost.pack(pady=5)

cost_input = Entry()                     #สร้างช่องรับค่าต้นทุน
cost_input.pack(pady=5)

button = Button(text='คำนวณ', command=calculate)   #ปุ่มสำหรับกดเพื่อคำนวณ
button.pack(pady=5)

result_output = Label(font='tahoma 12')             #แสดงผลลัพธ์การคำนวณ
result_output.pack(pady=5)

reset_button = Button(text="Reset", command=reset)
reset_button.pack(pady=10)

win.mainloop()