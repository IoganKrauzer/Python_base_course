import os
os.system("cls")
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
import math




def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in ("+","-","/","*"):
        value = value[:-1]
    if value[-2:] in "**":
        value = value[:-1]
    if operation[:3] == "log":
        calc.delete(0, tk.END)
        value = ''

    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calc_operation():
    value = calc.get()
    if value[:3] == 'log':
        value_h = int(value[4: -1])
        value = str(math.log10(value_h))
        calc.delete(0, tk.END)
        calc.insert(0, value)
    else:
        res_h = eval(value)
        calc.delete(0, tk.END)
        if res_h % 1 == 0:
            res_h = int(res_h)
            calc.insert(0, res_h)
        else:
            calc.insert(0, res_h)


def fct_func(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fct_func(num - 1)


def fact_show():
    value = calc.get()
    calc.delete(0, END)
    value = str(fct_func(int(value)))
    calc.insert(0, value)


def delete_ac():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def create_digit_button(digit):
    return ttk.Button(win, text=digit, command=lambda: add_digit(digit))


def create_operat_button(operation):
    return ttk.Button(win, text=operation,command=lambda: add_operation(operation))


def create_calc_button(ch_oper):
    return ttk.Button(win, text=ch_oper,command=calc_operation)


def create_del_button(ch_oper):
    return ttk.Button(win, text=ch_oper, command=lambda: delete_ac())


def delete_entry():
    calc.delete(0, ttk.END)


def create_entry(col):
        calc.grid(row=0,column=0, columnspan=col, stick='wens', padx=1, pady=1)   


def engin_but():
    global count
    if count % 2 == 0:
        win.geometry('280x200+1000+200')
        create_entry(7)
    else:
        win.geometry('160x200+1000+200')
        create_entry(4)  
    count+=1


def crt_but_for_sign_ch(ch_oper):
    return ttk.Button(win, text=ch_oper, command=sign_change)

# ------------Scientific Calculator---------------
def crt_swtch_for_engn(operation):
    return ttk.Button(win, text=operation, command=lambda: engin_but())


def crt_but_for_engin(operation):
    return ttk.Button(win, text=operation, command=lambda:add_operation(operation) )


def crt_but_fact(operation):
    return ttk.Button(win, text=operation, command=fact_show)


def crt_but_for_engin_sqr(operation):
    return ttk.Button(win, text=operation, command=lambda:square_root())


def crt_but_for_engin_trd(operation):
    return ttk.Button(win, text=operation, command=lambda:third_root())


def crt_but_for_engin_perc(operation):
    return ttk.Button(win, text=operation, command=lambda:percent())


def crt_but_for_engin_pow_2(operation):
    return ttk.Button(win, text=operation, command=lambda:pow_num(2))


def crt_but_for_engin_pow_3(operation):
    return ttk.Button(win, text=operation, command=lambda:pow_num(3))


def crt_but_for_engin_powX(operation):
    return ttk.Button(win, text=operation, command=lambda:add_operation('**'))


def crt_but_for_engin_bracket(operation):
    return ttk.Button(win, text=operation, command=lambda:add_bracket(operation))


def crt_but_for_engin_sin(operation):
    return ttk.Button(win, text=operation, command=lambda:trig_sin())


def crt_but_for_engin_cos(operation):
    return ttk.Button(win, text=operation, command=lambda:trig_cos())


def crt_but_for_engin_tan(operation):
    return ttk.Button(win, text=operation, command=lambda:trig_tan())


def crt_but_for_engin_pi(operation):
    return ttk.Button(win, text=operation, command=lambda:add_digit(str(round(math.pi, 9))))


def crt_but_for_engin_2pi(operation):
    return ttk.Button(win, text=operation, command=lambda:add_digit(str(2 * round(math.pi, 9))))


def crt_but_for_engin_log(operation):
    return ttk.Button(win, text=operation, command=lambda:add_operation('log('))


def square_root():
    value = calc.get()
    calc.delete(0, END)
    if int(value)>=0:
        value = eval(value+'**(1/2)')
    else:
        value = "ERROR"
    calc.insert(0, value)


def third_root():
    value = calc.get()
    calc.delete(0, END)
    if int(value)>=0:
        value = eval(value +'**(1/3)')
    else:
        value = "ERROR"
    calc.insert(0, value)


def percent():
    value = calc.get()
    value = eval(value + '/100')
    calc.delete(0, END)
    calc.insert(0, value)


def pow_num(num):
    value = calc.get()
    calc.delete(0, END)
    value = int(value) ** num
    calc.insert(0, value)


def add_bracket(operation):
    value = calc.get() + operation
    calc.delete(0, END)
    calc.insert(0, value)


def trig_sin():
    value = int(calc.get())
    calc.delete(0, END)
    value = str(round(math.sin(math.radians(value)), 7))
    calc.insert(0, value)


def trig_cos():
    value = int(calc.get())
    calc.delete(0, END)
    value = str(round(math.cos(math.radians(value)), 7))
    calc.insert(0, value)


def trig_tan():
    value = int(calc.get())
    calc.delete(0, END)
    value = str(round(math.tan(math.radians(value)), 7))
    calc.insert(0, value)


def sign_change():
    value = calc.get()
    calc.delete(0, END)
    if value[0]=='-':
        value = value[1:]
    else:
        value = '-' + value
    calc.insert(0, value)   




win = tk.Tk()
win.title('Калькулятор')
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
win.resizable(width=False, height=False)
win.geometry('160x200+1000+200')
win.config(bg='#bbd5fc')
count = 0

calc = tk.Entry(win, relief = RAISED, justify=tk.RIGHT, font=('Arial', 18), width=20 )
calc.insert(0, '0')
calc.grid(row=0,column=0, columnspan=4, stick='wens', padx=1, pady=1)

create_del_button('AC').grid(row=1, column=0, stick='wens', padx=1, pady=1)
create_digit_button('1').grid(row=4, column=0, stick='wens', padx=1, pady=1)
create_digit_button('2').grid(row=4, column=1, stick='wens', padx=1, pady=1)
create_digit_button('3').grid(row=4, column=2, stick='wens', padx=1, pady=1)
create_digit_button('4').grid(row=3, column=0, stick='wens', padx=1, pady=1)
create_digit_button('5').grid(row=3, column=1, stick='wens', padx=1, pady=1)
create_digit_button('6').grid(row=3, column=2, stick='wens', padx=1, pady=1)
create_digit_button('7').grid(row=2, column=0, stick='wens', padx=1, pady=1)
create_digit_button('8').grid(row=2, column=1, stick='wens', padx=1, pady=1)
create_digit_button('9').grid(row=2, column=2, stick='wens', padx=1, pady=1)
create_digit_button('0').grid(row=5, column=0, columnspan=2, sticky='wens', padx=1, pady=1)
create_digit_button('.').grid(row=5, column=2, stick='wens', padx=1, pady=1)
create_operat_button('*').grid(row=2, column=3, stick='wens', padx=1, pady=1)
create_operat_button('-').grid(row=3, column=3, stick='wens', padx=1, pady=1)
create_operat_button('+').grid(row=4, column=3, stick='wens', padx=1, pady=1)
create_operat_button('/').grid(row=1, column=3, stick='wens', padx=1, pady=1)
crt_but_for_sign_ch('+/-').grid(row=1, column=1, stick='wens', padx=1, pady=1)
create_calc_button('=').grid(row=5, column=3, stick='wens', padx=1, pady=1)
crt_swtch_for_engn('Engn').grid(row=1, column=2, stick='wens', padx=1, pady=1)

# Scientific Calculator
crt_but_for_engin_sin('sin').grid(row=1, column=4, stick='wens', padx=1, pady=1)
crt_but_for_engin_cos('cos').grid(row=1, column=5, stick='wens', padx=1, pady=1)
crt_but_for_engin_tan('tan').grid(row=1, column=6, stick='wens', padx=1, pady=1)
crt_but_for_engin_perc('%').grid(row=4, column=4, stick='wens', padx=1, pady=1)
# x^2 ; x^ 3
crt_but_for_engin_pow_2('x\u00B2').grid(row=2, column=4, stick='wens', padx=1, pady=1)     
crt_but_for_engin_pow_3('x\u00B3').grid(row=2, column=5, stick='wens', padx=1, pady=1)
crt_but_for_engin_powX('x\u207F').grid(row=2, column=6, stick='wens', padx=1, pady=1)
crt_but_for_engin_sqr('\u00B2\u221A').grid(row=3, column=4, stick='wens', padx=1, pady=1)
crt_but_for_engin_trd('\u00B3\u221A').grid(row=3, column=5, stick='wens', padx=1, pady=1)
crt_but_for_engin_log('log\u2081\u2080').grid(row=3, column=6, stick='wens', padx=1, pady=1)
crt_but_for_engin_pi('\u03C0').grid(row=4, column=6, stick='wens', padx=1, pady=1)
crt_but_fact('n!').grid(row=4, column=5, stick='wens', padx=1, pady=1)
crt_but_for_engin_bracket('(').grid(row=5, column=4, stick='wens', padx=1, pady=1)
crt_but_for_engin_bracket(')').grid(row=5, column=5, stick='wens', padx=1, pady=1)
crt_but_for_engin_2pi('2\u03C0').grid(row=5, column=6, stick='wens', padx=1, pady=1)

win.grid_columnconfigure(0, weight=30, minsize= 40)
win.grid_columnconfigure(1, weight=30, minsize= 40)
win.grid_columnconfigure(2, weight=30, minsize= 40)
win.grid_columnconfigure(3, weight=30, minsize= 40)
win.grid_columnconfigure(4, weight=30, minsize= 40)
win.grid_columnconfigure(5, weight=30, minsize= 40)
win.grid_columnconfigure(6, weight=30, minsize= 40)

win.rowconfigure(0, minsize= 50)
win.rowconfigure(1, minsize= 30)
win.rowconfigure(2, minsize= 30)
win.rowconfigure(3, minsize= 30)
win.rowconfigure(4, minsize= 30)
win.rowconfigure(5, minsize= 30)

win.mainloop()