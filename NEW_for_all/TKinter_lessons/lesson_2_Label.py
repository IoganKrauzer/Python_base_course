import os
os.system('clear')
import tkinter as tk
# Знакомство с виджет Label

win = tk.Tk()  
win.title('Мое первое графическое приложение')
win.geometry('400x400+600+200')
# свойства
label_1 = tk.Label(win, text='''Hello
                   world''',
                   bg='blue',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                    # padx=10, ->  отступы
                    # pady=10,
                    # width=10, -> высота в знаках
                    # height=10,
                    # anchor='n' размещение текста (n,w,e,s,nw,ne etc),
                    # relief=tk.RAISED, показывает обтекаемые границы
                    # bd = <цифра> -> ширина обтекаемой границы,
                    # justify=tk.RIGHT -> выравнивание текста 
                    justify=tk.CENTER



                   )
label_1.pack()
win.mainloop()