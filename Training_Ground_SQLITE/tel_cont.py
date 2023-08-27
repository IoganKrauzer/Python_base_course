import os
os.system('cls')
import sqlite3 as sq


# def create_table():
#     cur.execute("""CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT,
#         second_name TEXT,
#         telephone INTEGER,
#         sex INTEGER
#     )""")
#     con.commit()

with sq.connect('teleph_cont.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ava BLOB,
        first_name TEXT,
        second_name TEXT,
        telephone INTEGER,
        sex INTEGER
    )""")
    con.commit()
    

    # # first name TEXT NOT NULL, поле всегда должно быть заполнено
    # sex INTEGER DEAFAULT 1 поле по умолчанию ставится 1

    # cur.execute("INSERT INTO users(first_name,second_name,telephone,sex) VALUES('Sergey', 'Antipov', 12345, 1)")
    # con.commit()

    cur.execute("SELECT * from users")
    for raw in cur:
        print(raw)


    cur.execute("SELECT sex, telephone from users WHERE sex == 1")
    result = cur.fetchall()
    print(result)
    # SELECT ... FROM ... BETWEEN elem and elem2
    # ORDER BY old DESK по убыванию (ACS по возрастанию)
    # LIMIT <(огранич по записям)> [OFFSET offset <первые записи пропуст и вывести Лимит>]
    # LIMIT offset <смещение>, max
    # UPDATE table_name SET col_name = new znachenie <, n_col = new zna4> WHERE  условие
    # WHERE col_n LIKE 'name' (or 'A%' имена на букву А)
    # DELETE from name_t WHERE условие (rowid IN (num, num1))
    # -----------------------------------------------
    # SELECT count (user_id) подсчитывает, например, сумму игр) FROM games WHERE user_id = 1
    # count (user_id) as player
    # count(DISTINCT user_id) as player From games  уникальные игроки
    # sum(...) подсчитывает сумму
    # avr(...) среднее арифметическое по столбцу
    # min(...) минимальное
    # max(...) максимально
    # Группирование SELECT sum(score) as sum FROM games GROUP BY user_id  ORDER BY sum DESC => LIMIT 1
    # -------С В Я З Ы В А Н И Е    ТАБЛИЦ
    #  SELECT name, sex, games.score <обязательно в конце> FROM games <t_name>
    # JOIN users ON games.user_id = users.rowid
    #  или SELECT name, sex, games.score FROM users, games
    # LEFT JOIN
# SELECT name, sex, sum(games.score) as sum
# FROM games
# JOIN users ON games.user_id = users.rowid
# GOUP BY user_id
# ORDER BY score DESC
# ------------ВЛОженные запросы
# SELECT mark FROM marks WHERE id = 2 AND subject LIKE 'Си'
# WHERE mark > 3 AND subject LIKE 'Си'

# SELECT name, subject, mark from marks
# JOIN students ON students.rowid = marks.id
# WHERE mark > (SELECT mark FROM marks WHERE id = 2 AND subject LIKE 'Си') AND subject LIKE 'Си'
try:
    con = sq.connect('teleph_cont.db')
    cur = con.cursor()
except sq.Error as er:
    if con: 
        con.rollback()
        print('Ошибка выполнения запроса')
finally:
    if con:
        con.close()

for result in cur:
    print(result['model'], result['price'])

    #  Чтение изображений
    # n - номер аватарки
    def read_ava(n):   
        try:
            with open(f'avas{n}.png', 'rb') as i:
                return i.read()
        except IOError as er:
            print(er)
            return False
    
    def write_ava(name, data):
        try:
            with open(name, 'wb') as f:
                return f.write(data)
        except IOError as er:
            print(er)
            return False
        return True



    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']


    img = read_ava(1)
    if img:
        binary = sq.Binary(img)
        cur.execute("INSERT INTO users VALUES ('Sergey', 'Antipov', 9876, 1)", (binary))

    write_ava("out.png", img)



