import os
os.system('clear')
import tkinter as tk


win = tk.Tk()  
#  создаем переменную и помещаем главное окно
photo = tk.PhotoImage(file='team.png')
win.iconphoto(False, photo)
# создание логотипа в левом верхнем углу. На маке там переграждает меню мака
win.config(bg='#73BCA3')
# создаем цвет back ground
win.title('Мое первое графическое приложение')
# позволяет изменить заголовок
win.geometry('400x400+600+200')
# позволяет менять расположение окна в пикселях относительно левого верхнего угла
win.minsize(200,200)
win.maxsize(1000,1000)
# позволяет установаить макс и мин расширение для окна
win.resizable(True, True)
# можно менять размер окна мышкой (по ширине, по высоте)

win.mainloop()
#  запускаем цикл