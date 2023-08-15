# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,

# |     |  Х | 
# |     |  O |
# |     |  O |
# При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход
import os
from random import randint
os.system('cls')




def print_list(_crest_list):                # Распечатываем поле
    print("------------------")
    for i in _crest_list:
        print(i)
    print("------------------")


def que_start(_elem_start):                 # Выбираем очередность
    if _elem_start == 1 or _elem_start == 2:
        return _elem_start
    else:
        flag = True
        while flag:
            _elem_start = int(input("Вы не выбрали очередность. Нажмите 1 или 2: "))
            if _elem_start == 1 or _elem_start == 2:
                flag = False
    return _elem_start


def first_or_second_start(_player_element):   # Оповещение кто ходит первым
    if _player_element == 'X':
        print("Вы ходите первым. Удачи!")
    else:
        print("Вы ходите вторым. Удачи!")


def gererate_bot_position(_bot_element, _crest_list):  # Первая позиция бота 
    def generate_choices():
        _choice_num = randint(0,5)
        return _choice_num

    _list_with_coord = [None] * 2
    if _bot_element == 'X':
        flag = True
        while flag:
            choice_num = generate_choices()
            if choice_num == 0:
                _crest_list[0][0] = _bot_element
                _list_with_coord[0] = 0
                _list_with_coord[1] = 0
                flag = False
            elif choice_num == 1:
                _crest_list[0][2] = _bot_element
                _list_with_coord[0] = 0
                _list_with_coord[1] = 2  
                flag = False        
            elif choice_num == 2:
                _crest_list[2][0] = _bot_element
                _list_with_coord[0] = 2
                _list_with_coord[1] = 0
                flag = False
            elif choice_num == 3:
                _crest_list[2][2] = _bot_element
                _list_with_coord[0] = 2
                _list_with_coord[1] = 2
                flag = False
            elif choice_num == 4:
                _crest_list[1][1] = _bot_element
                _list_with_coord[0] = 1
                _list_with_coord[1] = 1 
                flag = False 
    else: 
        flag = True
        while flag:
            choice_num = generate_choices()
            if choice_num == 0 and _crest_list[0][0] == None:
                _crest_list[0][0] = _bot_element
                _list_with_coord[0] = 0
                _list_with_coord[1] = 0
                flag = False
            elif choice_num == 1 and _crest_list[0][2] == None:
                _crest_list[0][2] = _bot_element
                _list_with_coord[0] = 0
                _list_with_coord[1] = 2
                flag = False
            elif choice_num == 2 and _crest_list[2][0] == None:
                _crest_list[2][0] = _bot_element
                _list_with_coord[0] = 2
                _list_with_coord[1] = 0
                flag = False
            elif choice_num == 3 and _crest_list[2][2] == None:
                _crest_list[2][2] = _bot_element
                _list_with_coord[0] = 2
                _list_with_coord[1] = 2
                flag = False
            elif choice_num == 4 and _crest_list[1][1] == None:
                _crest_list[1][1] = _bot_element
                _list_with_coord[0] = 1
                _list_with_coord[1] = 1 
                flag = False
    return _list_with_coord     
   
            
def player_choice(_crest_list, _player_element):
    _raw = int(input("Введите номер строки: ")) - 1
    _column = int(input("Введите номер столбца: ")) - 1
    if _crest_list[_raw][_column] == None:           
        _crest_list[_raw][_column] = _player_element  
    else:
        flag = True
        while flag:
            print(f"Вы не можете туда поставить {_player_element}")
            _raw = int(input("Введите снова номер строки: ")) - 1
            _column = int(input(f"Введите снова номер столбца: ")) - 1
            if _crest_list[_raw][_column] == None:
                _crest_list[_raw][_column] = _player_element 
                flag = False


def field_check(_crest_list, _element, _player_element, _bot_element, _flag):      # Проверка поля для на ничью или кто победил
    def check_winner(_player_element, _b_element, _i):
        if _i == _player_element:
            winner = "Player"
            return winner
        elif _i == _b_element:
            winner = "Bot"
            return winner

    _check_n = None
    count = 0
    for i in _element:
        if i == _crest_list[0][0] == _crest_list[0][1] == _crest_list[0][2]:
            print(f"Победитель => {check_winner(_player_element, _bot_element, i)}")
            _flag = False
            break
        elif i == _crest_list[0][0] == _crest_list[1][0] == _crest_list[2][0]:
            print(f"Победитель => {check_winner(_player_element, _bot_element, i)}")
            _flag = False
            break
        elif i == _crest_list[0][0] == _crest_list[1][1] == _crest_list[2][2]:
            print(f"Победитель => {check_winner(_player_element, _bot_element, i)}")
            _flag = False
            break
        elif i == _crest_list[2][0] == _crest_list[2][1] == _crest_list[2][2]:
            print(f"Победитель => {check_winner(_player_element, _bot_element, i)}")
            _flag = False
            break
        elif i == _crest_list[0][2] == _crest_list[1][2] == _crest_list[2][2]:
            print(f"Победитель => {check_winner(_player_element, _bot_element, i)}") 
            _flag = False
            break                                                       
        elif i == _crest_list[1][0] == _crest_list[1][1] == _crest_list[1][2]:
            print(f"Победитель => {check_winner(_player_element, _bot_element, i)}")
            _flag = False
            break
        elif i == _crest_list[0][1] == _crest_list[1][1] == _crest_list[2][1]:
            print(f"Победитель => {check_winner(_player_element, _bot_element, i)}")
            _flag = False
            break
        else:
            for k in _crest_list:
                for p in range (len(_crest_list)):
                    if k[p] != _check_n:
                        count += 1
            if count == 9:
                print("Игра окончена. Ничья!")
                _flag = False
    return _flag


def bot_move(_crest_list, _list_with_coord, _bot_element):     # Ближайшее движение бота
    def help_move():
        _generate_coord = randint(0,2)
        return _generate_coord

    if _list_with_coord[0] - 1 < 0 and _list_with_coord[1] - 1 < 0:
        if _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] + 1] == None:
            _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] + 1] = _bot_element 
            _list_with_coord[0] = _list_with_coord[0] + 1
            _list_with_coord[1] = _list_with_coord[1] + 1
        elif  _crest_list[_list_with_coord[0]][_list_with_coord[1] + 1] == None:  
            _crest_list[_list_with_coord[0]][_list_with_coord[1] + 1] = _bot_element  
            _list_with_coord[0] = _list_with_coord[0]
            _list_with_coord[1] = _list_with_coord[1] + 1
        elif  _crest_list[_list_with_coord[0] + 1][_list_with_coord[1]] == None:  
            _crest_list[_list_with_coord[0] + 1][_list_with_coord[1]] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] + 1
            _list_with_coord[1] = _list_with_coord[1]
    elif _list_with_coord[0] - 1 < 0 and _list_with_coord[1] + 1 == len(_crest_list):
        if _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] - 1] == None:
            _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] - 1] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] + 1
            _list_with_coord[1] = _list_with_coord[1] - 1            
        elif  _crest_list[_list_with_coord[0]][_list_with_coord[1] - 1] == None:  
            _crest_list[_list_with_coord[0]][_list_with_coord[1] - 1] = _bot_element 
            _list_with_coord[0] = _list_with_coord[0] 
            _list_with_coord[1] = _list_with_coord[1] - 1  
        elif  _crest_list[_list_with_coord[0] + 1][_list_with_coord[1]] == None:  
            _crest_list[_list_with_coord[0] + 1][_list_with_coord[1]] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] + 1
            _list_with_coord[1] = _list_with_coord[1]

    elif _list_with_coord[0] + 1 == len(_crest_list) and _list_with_coord[1] - 1 < 0: 
        if _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] + 1] == None:
            _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] + 1] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] - 1
            _list_with_coord[1] = _list_with_coord[1] + 1 
        elif  _crest_list[_list_with_coord[0]][_list_with_coord[1] + 1] == None:  
            _crest_list[_list_with_coord[0]][_list_with_coord[1] + 1] = _bot_element 
            _list_with_coord[0] = _list_with_coord[0] 
            _list_with_coord[1] = _list_with_coord[1] + 1  
        elif  _crest_list[_list_with_coord[0] - 1][_list_with_coord[1]] == None:  
            _crest_list[_list_with_coord[0] - 1][_list_with_coord[1]] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] - 1
            _list_with_coord[1] = _list_with_coord[1] 

    elif _list_with_coord[0] + 1 == len(_crest_list) and _list_with_coord[1] + 1 == len(_crest_list):  
        if _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] - 1] == None:
            _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] - 1] = _bot_element 
            _list_with_coord[0] = _list_with_coord[0] - 1
            _list_with_coord[1] = _list_with_coord[1] - 1
        elif  _crest_list[_list_with_coord[0] - 1][_list_with_coord[1]] == None:  
            _crest_list[_list_with_coord[0] - 1][_list_with_coord[1]] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] - 1
            _list_with_coord[1] = _list_with_coord[1]    
        elif  _crest_list[_list_with_coord[0]][_list_with_coord[1] - 1] == None:  
            _crest_list[_list_with_coord[0]][_list_with_coord[1] - 1] = _bot_element
            _list_with_coord[0] = _list_with_coord[0]
            _list_with_coord[1] = _list_with_coord[1] - 1   

    elif _list_with_coord[0] - 1 == 0 and _list_with_coord[0] + 1 == len(_crest_list) and _list_with_coord[1] - 1 == 0 and _list_with_coord[1] + 1 == len(_crest_list):
        if _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] - 1] == None:
            _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] - 1] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] - 1
            _list_with_coord[1] = _list_with_coord[1] - 1 
        elif  _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] + 1] == None:  
            _crest_list[_list_with_coord[0] - 1][_list_with_coord[1] + 1] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] - 1
            _list_with_coord[1] = _list_with_coord[1] + 1    
        elif  _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] - 1] == None:  
            _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] - 1] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] + 1
            _list_with_coord[1] = _list_with_coord[1] - 1 
        elif  _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] + 1] == None:  
            _crest_list[_list_with_coord[0] + 1][_list_with_coord[1] + 1] = _bot_element
            _list_with_coord[0] = _list_with_coord[0] + 1
            _list_with_coord[1] = _list_with_coord[1] + 1 
    else:
        flag = True
        while flag:
            generate_coord_r = help_move()
            generate_coord_c = help_move()
            print("Raw: ", generate_coord_r)
            print("Col: ", generate_coord_c)
            if _crest_list[generate_coord_r][generate_coord_c] == None:
                _crest_list[generate_coord_r][generate_coord_c] = _bot_element
                _list_with_coord[0] = generate_coord_r
                _list_with_coord[1] = generate_coord_c
                flag = False

    return _list_with_coord




crest_list = [[None,None,None],
              [None,None,None],
              [None,None,None]]
element = ['X','O'] 
elem_start = int(input("Выберите очередность. < X > --- 1  < O > --- 2: "))
player_element = element[que_start(elem_start) - 1]
bot_element = element[2 - que_start(elem_start)]
print(f"Вы играете: {player_element}")
print(f"Бот играет: {bot_element}")
first_or_second_start(player_element)
print_list(crest_list)

if player_element == 'X':
    player_choice(crest_list, player_element)
    print_list(crest_list)
    list_with_coord = gererate_bot_position(bot_element, crest_list)
    print_list(crest_list)
    flag = True
    while flag:
        player_choice(crest_list, player_element)
        print_list(crest_list)
        flag = field_check(crest_list, element, player_element, bot_element, flag)
        list_with_coord = bot_move(crest_list, list_with_coord, bot_element)
        print_list(crest_list)
        flag = field_check(crest_list, element, player_element, bot_element, flag)

elif player_element == 'O':
    list_with_coord = gererate_bot_position(bot_element, crest_list)
    print_list(crest_list)
    flag = True
    while flag:
        player_choice(crest_list, player_element)
        flag = field_check(crest_list, element, player_element, bot_element, flag)
        print_list(crest_list)
        list_with_coord = bot_move(crest_list, list_with_coord, bot_element)
        print_list(crest_list)
        flag = field_check(crest_list, element, player_element, bot_element, flag)
