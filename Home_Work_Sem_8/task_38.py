# на Отлично в одного человека надо сделать консольное приложение 
# Телефонный справочник с внешним хранилищем информации, и чтоб был реализован основной функционал -
# просмотр, сохранение, импорт, поиск, удаление.
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
# для отлично в группах надо выполнить или ТГ бот или ГУИ (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД
# ГУИ можно сделать просто на EasyGUI или Tkinter

import os
os.system('cls')
import sqlite3 as sq




def create_table():

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        second_n TEXT, 
        first_n TEXT
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS telephone (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tel_number INTEGER 
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS relation (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        relations TEXT
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        tel_id INTEGER,
        rel_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (tel_id) REFERENCES telephone (id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (rel_id) REFERENCES relation (id) ON DELETE CASCADE ON UPDATE CASCADE
        )""")

 
def add_into_empty():

    cur.execute("SELECT * FROM users")
    if not cur.fetchall():
        cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Klomsel', 'Anton')")
        cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Bolgan', 'Mirgo')")
        cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Svintel', 'Perui')")
        cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Massaya', 'Zerka')")

    cur.execute("SELECT * FROM telephone")
    if not cur.fetchall():
        cur.execute("INSERT INTO telephone (tel_number) VALUES (64564)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (12323)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (21311)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (89031)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (89104)")

    cur.execute("SELECT * FROM relation")
    if not cur.fetchall():
        cur.execute("INSERT INTO relation (relations) VALUES ('friends')")
        cur.execute("INSERT INTO relation (relations) VALUES ('family')")
        cur.execute("INSERT INTO relation (relations) VALUES ('work')")
        cur.execute("INSERT INTO relation (relations) VALUES ('enemy')")

    cur.execute("SELECT * FROM contacts")
    if not cur.fetchall():
        cur.execute("INSERT INTO contacts (user_id, tel_id, rel_id) VALUES (1, 1, 4)")
        cur.execute("INSERT INTO contacts (user_id, tel_id, rel_id) VALUES (1, 2, 4)")
        cur.execute("INSERT INTO contacts (user_id, tel_id, rel_id) VALUES (2, 3, 2)")
        cur.execute("INSERT INTO contacts (user_id, tel_id, rel_id) VALUES (3, 4, 1)")
        cur.execute("INSERT INTO contacts (user_id, tel_id, rel_id) VALUES (4, 5, 3)")


def show_all():
    cur.execute("SELECT second_n, first_n, tel_number, relations FROM contacts JOIN users ON contacts.user_id = users.id \
        JOIN telephone ON contacts.tel_id = telephone.id JOIN relation ON contacts.rel_id = relation.id ORDER BY second_n ASC")
    for row in cur:
        f = '{0:<8} | {1:<8} | {2:<8} | {3:<5}'.format(*row)
        print(f)


def add_user():
    surname = input("Введите фамилию пользователя: ").capitalize()
    name = input("Введите имя пользователя: ").capitalize()
    cur.execute(f"INSERT INTO users VALUES(NULL,'{surname}','{name}')")
    last_id = cur.lastrowid
    cur.execute(f"INSERT INTO contacts (user_id) VALUES({last_id})")

    tel = int(input("Введите номер телефона: "))
    cur.execute(f"INSERT INTO telephone VALUES(NULL, {tel})")
    tel_i = cur.lastrowid

    cur.execute(f"UPDATE contacts SET tel_id = {tel_i} WHERE user_id = '{last_id}'")
 
    print("Выберите группу контакта \n 1 - friends \n 2 - family \n 3 - work \n 4 - enemy")
    rel_hlp = input("Введите цифру: ")
    while True:
        if rel_hlp == "1":
            cur.execute(f"UPDATE contacts SET rel_id = '1' WHERE user_id = '{last_id}'")
            break
        elif rel_hlp == "2":
            cur.execute(f"UPDATE contacts SET rel_id = '2' WHERE user_id = '{last_id}'")
            break
        elif rel_hlp == "3":
            cur.execute(f"UPDATE contacts SET rel_id = '3' WHERE user_id = '{last_id}'")
            break
        elif rel_hlp == "4":
            cur.execute(f"UPDATE contacts SET rel_id = '4' WHERE user_id = '{last_id}'")
            break


def search_user ():
    sec_n = input("Введите фамилию пользователя: ").capitalize()
    cur.execute(f"SELECT second_n, first_n, tel_number, relations FROM contacts JOIN users ON contacts.user_id = users.id \
        JOIN telephone ON contacts.tel_id = telephone.id JOIN relation ON contacts.rel_id = relation.id WHERE second_n = '{sec_n}'")
    for row in cur:
        f = '{0:<8} | {1:<8} | {2:<8} | {3:<5}'.format(*row)
        print(f)
  

def update_data():
    while True:
        answer = input("В каком поле вы хотите внести изменения?\n 1 - Фамилия\n 2 - Телефон\n 3 - Группа\n 0 - Выход\n ")
        if answer == '1':
            sec_n_q = input("Введите фамилию которую хотите изменить: ").capitalize()
            sec_n = input("Введите новую фамилию пользователя: ").capitalize()
            cur.execute(f"UPDATE users SET second_n = '{sec_n}' WHERE second_n = '{sec_n_q}'")
            continue
        elif answer == '2':
            sec_n = input("Введите фамилию пользователя телефон которого хотите изменить: ").capitalize()
            cur.execute(f"SELECT second_n, first_n, tel_number FROM contacts JOIN users ON contacts.user_id = users.id \
                JOIN telephone ON contacts.tel_id = telephone.id  WHERE second_n = '{sec_n}'")
            for row in cur:
                f = '{0:<8} | {1:<8} | {2:<8}'.format(*row)
                print(f)
            old_tel = int(input("Введите телефонный номер который хотите изменить: "))
            new_tel = int(input("Введите новый телефонный номер: "))
            cur.execute(f"UPDATE telephone SET tel_number = {new_tel} WHERE tel_number = '{old_tel}'")

        elif answer == '3':
            sec_n_q = input("Введите фамилию пользователя группу которого хотите изменить: ").capitalize()
            res = int(input("Выберите новую группу контакта: \n 1 - friends\n 2 - family\n 3 - work\n 4 - enemy\n "))
            cur.execute(f"UPDATE contacts SET rel_id = {res} WHERE user_id = (SELECT id FROM users WHERE second_n = '{sec_n_q}')")
            continue
        elif answer == '0':
            break
    

def delete_record():
    sec_n = input("Введите фамилию пользователя: ").capitalize()
    cur.execute(f"SELECT second_n, first_n, tel_number, relations FROM contacts JOIN users ON contacts.user_id = users.id \
        JOIN telephone ON contacts.tel_id = telephone.id JOIN relation ON contacts.rel_id = relation.id WHERE second_n = '{sec_n}'")
    for row in cur:
        f = '{0:<8} | {1:<8} | {2:<8} | {3:<5}'.format(*row)
        print(f)
    answer = input('Вы точно хотите удалить этого пользователя? Y/N: ').upper()
    if answer == 'Y':
        cur.execute("DELETE FROM users WHERE second_n = ?", (f'{sec_n}',))
    else: 
        return
   

def print_info():
    print("/all => Выводит информацию по контактам")
    print("/add => Добавляет контакт")
    print("/del => Удаляет контакт")
    print("/up => Позволяет внести изменения в контакт")
    print("/info => Информация по доступным командам")
    print("/save => Сохранить внесенные изменения")
    print("/search => Поиск контакта по фамилии")
    print("/stop => Выйти из меню команд")
    print("Специфические команды:\n/sec -> Удаляет все таблицы\n/adm -> Создает заново таблицы и заполняет их")



def secret_command():
    cur.execute("DROP TABLE IF EXISTS contacts")
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("DROP TABLE IF EXISTS telephone")
    cur.execute("DROP TABLE IF EXISTS relation")




with sq.connect("cont_tel.db") as con:
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys=True")
    create_table()
    add_into_empty()
  

    while True:
        command = input("\nВведите команду: ")
        command = command.lower()
        if command == "/all":
            show_all()
        elif command == "/stop":
            break
        elif command == "/add":
            add_user()
        elif command == "/save":
            con.commit()
        elif command == "/search":
            search_user()
        elif command == "/del":
            delete_record()
        elif command == "/up":
            update_data()
        elif command == "/info":
            print_info()
        elif command == "/sec":
            secret_command()
        elif command == "/adm":
            create_table()
            add_into_empty()


