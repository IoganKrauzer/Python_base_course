import os
os.system('clear')
import tkinter as tk
# Знакомство с виджет Button

def say_hello():
    print('Hello, dude!')


def add_label():
    label_1 = tk.Label(win,text='new')
    label_1.pack()


def counter():
    global count
    count+=1
    btn_4['text'] = f"Counts: {count}"


count = 0
win = tk.Tk()  
win.title('Мое первое графическое приложение')
win.geometry('400x400+600+200')
win.config(bg='#73BCA3')
btn_1 = tk.Button(win, text='Hello',
                  command=say_hello,
                  bg='blue'
                  )
btn_2 = tk.Button(win, text='Add new label!',
                  command=add_label,
                  bg='red'
                  )
btn_3 = tk.Button(win, text='Add_label_lambda',
                  command=lambda: tk.Label(win, text='new Lambda').pack()
                  )
btn_4 = tk.Button(win, text=f"Counts: {count}",
                  command=counter,
                  bg='#73BCA3',
                  activebackground='#73BCA3',
                  font=('Arial', 18, 'bold'),
                  state=tk.NORMAL
                  )
btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()
win.mainloop()