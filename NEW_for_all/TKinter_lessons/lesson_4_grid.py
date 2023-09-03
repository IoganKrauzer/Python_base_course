import os
os.system('clear')
import tkinter as tk
# как размещать с помощью виджетов метод grid()


win = tk.Tk()  
win.title('Мое первое графическое приложение')
win.geometry('400x400+600+200')
# btn_1 = tk.Button(win, text='Hello 1')
# btn_2 = tk.Button(win, text='Hello 2')
# btn_3 = tk.Button(win, text='Hello 3')
# btn_4 = tk.Button(win, text='Hello 4')
# btn_5 = tk.Button(win, text='Hello 5')
# btn_6 = tk.Button(win, text='Hello 6')
# btn_7 = tk.Button(win, text='Hello 7')
# btn_8 = tk.Button(win, text='Hello 8')

# btn_1.grid(row=0, column=0)
# btn_2.grid(row=0, column=1)
# btn_3.grid(row=1, column=0)
# btn_4.grid(row=1, column=1)
# btn_5.grid(row=2, column=0)
# btn_6.grid(row=2, column=1)
# btn_7.grid(row=3, column=0, columnspan=2, stick='we')
# btn_8.grid(row=0,column=3, rowspan=4, stick='ns')
# # Объединяем ячейки

# ---------------------------------
for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'Hello {i} {j}').grid(row=i, column=j, stick='we')


win.columnconfigure(0, minsize=200)
win.columnconfigure(1, minsize=100)
# задаем минимальные значения для колонок

win.mainloop()