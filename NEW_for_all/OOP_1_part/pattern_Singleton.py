import os
os.system('clear')

class DataBase:

    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    

    def __del__(self):
        DataBase.__instance = None


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port


    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')


    def close(self):
        print('Звкрытие БД')


    def read(self):
        return 'данные из БД'
    

    def write(self, data):
        print(f'Запись в БД {data}')


db = DataBase('root', 123, 80)
db_2 = DataBase('root2', 321, 40)
print(id(db), id(db_2))