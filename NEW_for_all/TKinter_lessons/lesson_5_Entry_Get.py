import os
os.system('clear')
import tkinter as tk
# как размещать с помощью виджетов ENTRY


def get_entry():
    value = name.get()
    # get() получить информацию
    if value:
        print(value)
    else:
        print('Empty Entry')


def delete_entry():
    name.delete(0,tk.END)
    password.delete(0, tk.END)
    # tk.END == 'end'  -> удалить все


def submit():
    print(name.get())
    print(password.get())
    delete_entry()



win = tk.Tk()  
win.title('Мое первое графическое приложение')
win.geometry('400x400+600+200')

name = tk.Entry(win)
password = tk.Entry(win,show='*')
# show='<>' помогает скрыть ввод/ Пример ввод пароля
name.grid(row=0, column=1)
password.grid(row=1, column=1)
tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='w')
tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, sticky='we')
tk.Button(win, text='delete', command=delete_entry).grid(row=2, column=1, sticky='we')
tk.Button(win, text='submit', command=submit).grid(row=3, column=0, sticky='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'hello'))\
    .grid(row=2, column=2, sticky='we')


win.columnconfigure(0, minsize=100)
win.columnconfigure(1, minsize=100)





win.mainloop()