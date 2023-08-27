import os
os.system('cls')
from random import *
import json
games = []



def save():
    with open('games.json', 'w', encoding= 'utf - 8') as gm:
        gm.write(json.dumps(games, ensure_ascii=False))
    print('Список игр успешно сохранен в файле games.json')


def load():
    with open('games.json', 'r', encoding='utf-8') as gm:
        games = json.load(gm)
    print('Игротека успешно загружена')



# games = []
games.append('Final  Fantasy')
games.append('Legends of Heroes')
games.append('Front Mission')
games.append('Chrono Cross')
games.append('Dragon Quest')
while True:
    command = input('Введите команду: ')
    if command == '/start':
        print('Бот начал свою работу')
    elif command == '/stop':
        print('Бот остановил свою работу') 
        break
    elif command == '/all':
        print('Весь список выведен на экран')
        print(', '.join(games))
    elif command == '/add':
        games.append(input('Введите наименование игры: '))
        print(f'Добавлена игра')
    elif command == '/help':
        print('Здесь какой-то мануал')
    elif command == '/del':
        f = input('Введите наименование игры: ')
        '''
        if f in games:
            games.remove(f)
            print('Игра успешно удалена.')
        else:
            print('Такой игры в списке нет')
        '''
        try:
            games.remove(f)
            print('Игра успешно удалена.')
        except:
            print('Такой игры в списке нет')
    elif command == '/random':
        # index = randint(0, len(games) - 1)
        # print(f'Рекомендуем игру {games[index]}')
        
        print(f'Рекомендуем игру {choice(games)}')
    elif command == '/save':
        save()
    elif command =='/load':
        # with open('games.json', 'r', encoding='utf-8')as gm:
        #     games = json.load(gm)
        # print('Игротека успешно загружена')
        load()
    else:
        print('Введена неопознанная команда. Просьба изучить мануал через команду /help')
       