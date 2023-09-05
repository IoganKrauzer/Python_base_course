import os
os.system('cls')
import sqlite3 as sq




def create_table():

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        second_n TEXT, 
        first_n TEXT
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS telephone (
        id INTEGER PRIMARY KEY,
        tel_number INTEGER
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS relation (
        id INTEGER PRIMARY KEY, 
        relations TEXT
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
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
        cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Massaya', 'Telka')")

    cur.execute("SELECT * FROM telephone")
    if not cur.fetchall():
        cur.execute("INSERT INTO telephone (tel_number) VALUES (89257655664)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (89108761230)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (89163211299)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (89031897645)")
        cur.execute("INSERT INTO telephone (tel_number) VALUES (89104557318)")

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
    cur.execute(f"INSERT INTO users VALUES(NULL, '{surname}','{name}')")
    last_id = cur.lastrowid
    con.commit()
 
    count_hlp = int(input("Сколько телефонов у пользователя? "))
    i = 0
    while i < count_hlp:
        tel = int(input("Введите номер телефона: "))
        cur.execute(f"INSERT INTO telephone (tel_number) VALUES ({last_id}, {tel})")
        i += 1

    print("Кем вам приходится пользователь \n 1 - friends \n 2 - family \n 3 - work \n 4 - enemy")
    rel_hlp = int(input("Введите цифру: "))
    while True:
        if rel_hlp == 1:
            cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'friends')")
            break
        elif rel_hlp == 2:
            cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'family')")
            break
        elif rel_hlp == 3:
            cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'work')")
            break
        elif rel_hlp == 4:
            cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'enemy')")
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
            cur.execute(f"UPDATE users SET second_n = '{sec_n} WHERE second_n = {sec_n_q}'")

        elif answer == '2':
            sec_n = input("Введите фамилию пользователя телефон которого хотите изменить: ").capitalize()
            cur.execute(f"SELECT second_n, first_n, tel_number FROM contacts JOIN users ON contacts.user_id = users.id \
                JOIN telephone ON contacts.tel_id = telephone.id  WHERE second_n = '{sec_n}'")
            for row in cur:
                f = '{0:<8} | {1:<8} | {2:<8}'.format(*row)
                print(f)



        elif answer == '3':
            sec_n_q = input("Введите фамилию пользователя группу которого хотите изменить: ").capitalize()
            res = int(input("Выберите новую группу контакта: \n 1 - friends\n 2 - family\n 3 - work\n 4 - enemy\n "))
            cur.execute(f"UPDATE contacts SET rel_id = {res} WHERE user_id = (SELECT id FROM users WHERE second_n = '{sec_n_q}')")
            continue
        elif answer == '0':
            break
    
    # surname_h = input("Введите фамилию: ")
    # new_tel = int(input("Введите новый номер телефона: "))
    # cur.execute(f"UPDATE telephone SET tel_number {new_tel} WHERE")


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




with sq.connect("cont_tel.db") as con:
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys=True")
    # cur.execute("DROP TABLE IF EXISTS relation")
    # cur.execute("DROP TABLE IF EXISTS telephone")
    # cur.execute("DROP TABLE IF EXISTS users")
    # cur.execute("DROP TABLE IF EXISTS contacts")
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


        








# -------------------------------------------------------------------------------------------------------------------------

# def create_table():

#     cur.execute("""CREATE TABLE IF NOT EXISTS users 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         second_n TEXT, 
#         first_n TEXT
#         )""")

#     cur.execute("""CREATE TABLE IF NOT EXISTS telephone 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER, 
#         tel_number INTEGER,
#         FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
#         )""")

#     cur.execute("""CREATE TABLE IF NOT EXISTS relation 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         user_id INTEGER,
#         relations TEXT,
#         FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
#         )""")

 
# def add_into_empty():

#     cur.execute("SELECT * FROM users")
#     if not cur.fetchall():
#         cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Klomsel', 'Anton')")
#         cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Bolgan', 'Mirgo')")
#         cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Svintel', 'Perui')")
#         cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Massaya', 'Telka')")

#     cur.execute("SELECT * FROM telephone")
#     if not cur.fetchall():
#         cur.execute("INSERT INTO telephone (user_id, tel_number) VALUES (1, 89257655664)")
#         cur.execute("INSERT INTO telephone (user_id, tel_number) VALUES (1, 89108761230)")
#         cur.execute("INSERT INTO telephone (user_id, tel_number) VALUES (2, 89163211299)")
#         cur.execute("INSERT INTO telephone (user_id, tel_number) VALUES (3, 89031897645)")
#         cur.execute("INSERT INTO telephone (user_id, tel_number) VALUES (4, 89104557318)")

#     cur.execute("SELECT * FROM relation")
#     if not cur.fetchall():
#         cur.execute("INSERT INTO relation (user_id, relations) VALUES (4, 'friends')")
#         cur.execute("INSERT INTO relation (user_id, relations) VALUES (2, 'family')")
#         cur.execute("INSERT INTO relation (user_id, relations) VALUES (1, 'work')")
#         cur.execute("INSERT INTO relation (user_id, relations) VALUES (3, 'enemy')")


# def show_all():
#     cur.execute("SELECT second_n, first_n, tel_number, relations FROM telephone JOIN users ON telephone.user_id = users.id \
#         JOIN relation ON telephone.user_id = relation.user_id ORDER BY second_n ASC")
#     for row in cur:
#         f = '{0:<8} | {1:<8} | {2:<8} | {3:<5}'.format(*row)
#         print(f)


# def add_user():
#     surname = input("Введите фамилию пользователя: ").capitalize()
#     name = input("Введите имя пользователя: ").capitalize()
#     cur.execute(f"INSERT INTO users VALUES(NULL, '{surname}','{name}')")
#     last_id = cur.lastrowid
#     con.commit()
 
#     count_hlp = int(input("Сколько телефонов у пользователя? "))
#     i = 0
#     while i < count_hlp:
#         tel = int(input("Введите номер телефона: "))
#         cur.execute(f"INSERT INTO telephone (user_id, tel_number) VALUES ({last_id}, {tel})")
#         i += 1

#     print("Кем вам приходится пользователь \n 1 - friends \n 2 - family \n 3 - work \n 4 - enemy")
#     rel_hlp = int(input("Введите цифру: "))
#     while True:
#         if rel_hlp == 1:
#             cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'friends')")
#             break
#         elif rel_hlp == 2:
#             cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'family')")
#             break
#         elif rel_hlp == 3:
#             cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'work')")
#             break
#         elif rel_hlp == 4:
#             cur.execute(f"INSERT INTO relation (user_id, relations) VALUES ({last_id}, 'enemy')")
#             break


# def search_user ():
#     sec_n = input("Введите фамилию пользователя: ").capitalize()
#     cur.execute(f"SELECT second_n, first_n, tel_number, relations FROM telephone JOIN users ON telephone.user_id = users.id \
#         JOIN relation ON telephone.user_id = relation.user_id WHERE second_n = '{sec_n}'")
#     for row in cur:
#         f = '{0:<8} | {1:<8} | {2:<8} | {3:<5}'.format(*row)
#         print(f)
  

# # def update_tel():
# #     surname_h = input("Введите фамилию: ")
# #     new_tel = int(input("Введите новый номер телефона: "))
# #     cur.execute(f"UPDATE telephone SET tel_number {new_tel} WHERE")


# def delete_record():
#     sur_var = input("Введите фамилию пользователя: ").capitalize()
#     cur.execute(f"SELECT second_n, first_n, tel_number, relations FROM telephone JOIN users ON telephone.user_id = users.id \
#         JOIN relation ON telephone.user_id = relation.user_id WHERE second_n = '{sur_var}'")
#     for row in cur:
#         f = '{0:<8} | {1:<8} | {2:<8} | {3:<5}'.format(*row)
#         print(f)
#     answer = input('Вы точно хотите удалить этого пользователя? Y/N: ').upper()
#     if answer == 'Y':
#         cur.execute("DELETE FROM users WHERE second_n = '{sur_var}'")
#         # cur.execute("DELETE FROM users WHERE second_n = '{sur_var}'")
#     else: 
#         return




# with sq.connect("cont_tel.db") as con:
#     cur = con.cursor()
#     cur.execute("PRAGMA foreign_keys=True")
#     cur.execute("DROP TABLE IF EXISTS relation")
#     cur.execute("DROP TABLE IF EXISTS telephone")
#     cur.execute("DROP TABLE IF EXISTS users")
#     create_table()
#     add_into_empty()
  

#     while True:
#         command = input("\nВведите команду: ")
#         command = command.lower()
#         if command == "/all":
#             show_all()
#         elif command == "/stop":
#             break
#         elif command == "/add":
#             add_user()
#         elif command == "/save":
#             con.commit()
#         elif command == "/search":
#             search_user()
#         elif command == "/del":
#             delete_record()



# ----------------------------------------------------------------------------------------------------------------------------------



# print ("SQLite Version is:", sq.sqlite_version)
# print ("DB-API Version is:", sq.version)








    # cur.execute("SELECT * FROM users ORDER BY second_n ASC")
    # for row in cur.fetchall():
    #     print("   ".join(map(str, row)))


# SELECT name, sex, games.score FROM games
# JOIN users ON games.user_id = users.rowid





# --------------------------------------------------------------------------------------

# def create_table():

#     # cur.execute("""CREATE TABLE IF NOT EXISTS users 
#     #     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #     second_n TEXT, 
#     #     first_n TEXT
#     #     )""")

#     cur.execute("""CREATE TABLE IF NOT EXISTS telephone 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_cont INTEGER, 
#         tel_number INTEGER,
#         FOREIGN KEY (user_cont) REFERENCES contacts (id)
#         )""")

#     cur.execute("""CREATE TABLE IF NOT EXISTS sex 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         sex_col TEXT
#         )""")

#     cur.execute("""CREATE TABLE IF NOT EXISTS relations 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         relations TEXT
#         )""")

#     cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         second_name TEXT,
#         first_name TEXT,
#         phone_id INTEGER,
#         sex_id INTEGER,
#         relatives_id INTEGER,
#         FOREIGN KEY (phone_id) REFERENCES telephone (id),
#         FOREIGN KEY (sex_id) REFERENCES sex (id),
#         FOREIGN KEY (relatives_id) REFERENCES relations (id)
#         )""")


# def add_into_empty():
    
#     # cur.execute("SELECT * FROM users")
#     # if not cur.fetchall():
#     #     cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Царкан', 'Амир')")
#     #     cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Бульчан', 'Маргарита')")
#     #     cur.execute("INSERT INTO users (second_n, first_n) VALUES ('Свинтий', 'Перуй')")

#     cur.execute("SELECT * FROM telephone")
#     if not cur.fetchall():
#         cur.execute("INSERT INTO telephone (user_cont, tel_number) VALUES (1, 89257655664)")
#         cur.execute("INSERT INTO telephone (user_cont, tel_number) VALUES (1, 89108761230)")
#         cur.execute("INSERT INTO telephone (user_cont, tel_number) VALUES (2, 89163211299)")
#         cur.execute("INSERT INTO telephone (user_cont, tel_number) VALUES (3, 89031897645)")

#     cur.execute("SELECT * FROM sex")
#     if not cur.fetchall():
#         cur.execute("INSERT INTO sex (sex_col) VALUES ('man')")
#         cur.execute("INSERT INTO sex (sex_col) VALUES ('woman')")

#     cur.execute("SELECT * FROM relations")
#     if not cur.fetchall():
#         cur.execute("INSERT INTO relations (relations) VALUES ('friends')")
#         cur.execute("INSERT INTO relations (relations) VALUES ('family')")
#         cur.execute("INSERT INTO relations (relations) VALUES ('work')")
#         cur.execute("INSERT INTO relations (relations) VALUES ('enem')")

#     cur.execute("SELECT * FROM contacts")
#     if not cur.fetchall():
#         cur.execute("INSERT INTO contacts (second_name, first_name, phone_id, sex_id, relatives_id) VALUES ('Царкан', 'Амир', 1, 1, 3)")
#         cur.execute("INSERT INTO contacts (second_name, first_name, phone_id, sex_id, relatives_id) VALUES ('Бульчан', 'Маргарита', 2, 2, 1)")
#         cur.execute("INSERT INTO contacts (second_name, first_name, phone_id, sex_id, relatives_id) VALUES ('Свинтий', 'Перуй', 3, 1, 2)")

#     con.commit()

      

# def show_table():

#     # cur.execute("SELECT * FROM users")
#     # for raw in cur:
#     #     print(raw)
#     # print()
    
#     cur.execute("SELECT * FROM contacts")
#     for raw in cur:
#         print(raw)
#     print()

#     cur.execute("SELECT * FROM telephone")
#     for raw in cur:
#         print(raw)
#     print()

#     cur.execute("SELECT * FROM sex")
#     for raw in cur:
#         print(raw)
#     print()

#     cur.execute("SELECT * FROM relations")
#     for raw in cur:
#         print(raw)

# # def check_tr():
# #     cur.execute("SELECT users.second_n, users.first_n, telephone.tel_number, sex.sex_col, relations.relations FROM contacts JOIN contacts ON contacts.second_name = users.id")
# #     for row in cur:
# #         print(row)
    

# with sq.connect("cont_tel.db") as con:
#     cur = con.cursor()
#     cur.execute("PRAGMA foreign_keys=True")
#     cur.execute("DROP TABLE IF EXISTS contacts")
#     cur.execute("DROP TABLE IF EXISTS relations")
#     cur.execute("DROP TABLE IF EXISTS sex")
#     cur.execute("DROP TABLE IF EXISTS telephone")
#     cur.execute("DROP TABLE IF EXISTS users")
#     create_table()
#     add_into_empty()
#     show_table()
#     # check_tr()
        



















    # con_table = [('Царкан', 'Амир', 1, 1, 3), ('Бульчан', 'Маргарита', 2, 2, 1), ('Свинтий', 'Перуй', 3, 1, 2)]
    # tel_table = [(89257655664), (89163211299), (89031897645)]
    # sex_table = [('man'), ('woman')]
    # rel_table = [('friends'), ('family'), ('work'), ('enem')]

    # sql_tel = "INSERT INTO telephone (tel_number) VALUES (?)"
    # sql_sex = "INSERT INTO sex (sex_col) VALUES (?)"
    # sql_rel = "INSERT INTO relations (relations) VALUES (?)"
    # sql_con = "INSERT INTO contacts (second_name, first_name, phone_id, sex_id, relatives_id) VALUES (?, ?, ?, ?, ?)"


    # cur.executemany(sql_tel, tel_table)
    # cur.executemany(sql_sex, sex_table)
    # cur.executemany(sql_rel, rel_table)
    # cur.executemany(sql_con, con_table)
