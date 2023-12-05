from tkinter import *
from tkinter import messagebox

profit = 0
percent = 0
result = ''
def calculate():
    global result
    try:
        profit = float(income_input.get()) - float(cost_input.get())
        percent = profit / float(cost_input.get()) * 100
        if profit > 0:
            result = "ได้กำไร "+ str(abs(profit)) +" บาท \nคิดเป็น "+ str(abs(percent)) +" %"
            result_output.config(text=result)
        elif profit <0:
            result = 'ขาดทุน '+str(abs(profit))+" บาท \nคิดเป็น "+ str(abs(percent)) + " %" 
            result_output.config(text=result)
    except:
        messagebox.showerror("Error", "ข้อมูลไม่ถูกต้อง")
win = Tk()
win.title('Profit and Loss Calculator')
win.geometry('800x600')
win.config(bg='#B0E0E6')
win.option_add('*Label.background', '#B0E0E6')

label_head1 = Label(text="โปรแกรมคำนวณกำไร-ขาดทุน", font='tahoma 16 bold')
label_head1.pack()

label_income = Label(text='รายได้' , font='tahoma 14 ')
label_income.pack()

income_input = Entry()
income_input.pack()

label_cost = Label(text='ต้นทุน', font='tahoma 14')
label_cost.pack()

cost_input = Entry()
cost_input.pack()

button = Button(text='คำนวณ', command=calculate)
button.pack()
result_output = Label()
result_output.pack()

win.mainloop()