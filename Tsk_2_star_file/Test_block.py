import os
from random import randint
os.system('cls')




def print_list(_crest_list):
    print("------------------")
    for i in _crest_list:
        print(i)
    print("------------------")


def bot_move(_crest_list, raw, col, bot_element):
    flag = True
    while flag:
        if raw - 1 < 0 and col - 1 < 0:
            if _crest_list[raw + 1][col + 1] == None:
                _crest_list[raw + 1][col + 1] = bot_element   
            elif  _crest_list[raw][col + 1] == None:  
                _crest_list[raw][col + 1] = bot_element  
            elif  _crest_list[raw + 1][col] == None:  
                _crest_list[raw + 1][col] = bot_element

        elif raw - 1 < 0 and col + 1 == len(_crest_list):
            if _crest_list[raw + 1][col - 1] == None:
                _crest_list[raw + 1][col - 1] = bot_element   
            elif  _crest_list[raw][col - 1] == None:  
                _crest_list[raw][col - 1] = bot_element    
            elif  _crest_list[raw + 1][col] == None:  
                _crest_list[raw + 1][col] = bot_element

        elif raw + 1 == len(_crest_list) and col - 1 < 0: 
            if _crest_list[raw - 1][col + 1] == None:
                _crest_list[raw - 1][col + 1] = bot_element   
            elif  _crest_list[raw][col + 1] == None:  
                _crest_list[raw][col + 1] = bot_element    
            elif  _crest_list[raw - 1][col] == None:  
                _crest_list[raw - 1][col] = bot_element 

        elif raw + 1 == len(_crest_list) and col + 1 == len(_crest_list):  
            if _crest_list[raw - 1][col - 1] == None:
                _crest_list[raw - 1][col - 1] = bot_element   
            elif  _crest_list[raw - 1][col] == None:  
                _crest_list[raw - 1][col] = bot_element    
            elif  _crest_list[raw][col - 1] == None:  
                _crest_list[raw][col - 1] = bot_element     

        elif raw - 1 == 0 and raw + 1 == len(_crest_list) and col - 1 == 0 and col + 1 == len(_crest_list):
            if _crest_list[raw - 1][col - 1] == None:
                _crest_list[raw - 1][col - 1] = bot_element   
            elif  _crest_list[raw - 1][col + 1] == None:  
                _crest_list[raw - 1][col + 1] = bot_element    
            elif  _crest_list[raw + 1][col - 1] == None:  
                _crest_list[raw + 1][col - 1] = bot_element 
            elif  _crest_list[raw + 1][col + 1] == None:  
                _crest_list[raw + 1][col + 1] = bot_element 
        flag = False
    # return crest_list




crest_list = [[None,None,None],
              [None,None,None],
              [None,None,None]]

_raw = 0
_col = 0 
element_start = 'X'
_bot_element = 'O'

# print_list(crest_list)
# bot_int(crest_list, _raw, _col, _bot_element)
# print_list(crest_list)



        # if raw == 0 and col == 0:
        #     if _crest_list
        # elif raw == 0 and col == 2:
        # elif raw == 2 and col == 0:
        # elif raw == 2 and col == 2:
        # elif raw == 1 and col == 1:    














              
# def gererate_bot_position(_crest_list):
#     _bot_element = 'X'
#     def generate_choices(_bot_element):
#         choice_num = randint(0, 4)
#         print(choice_num)
#         if _bot_element == 'X':
#             if choice_num == 0:
#                 _crest_list[0][0] = 'X'
#                 print(_crest_list)
#                 _list_with_coord = [0, 0]
#                 print(_list_with_coord)
#                 return _list_with_coord
#             elif choice_num == 1:
#                 _crest_list[0][2] = 'X'
#                 _list_with_coord = [0, 2]
#                 return _list_with_coord
#             elif choice_num == 2:
#                 _crest_list[2][0] = 'X'
#                 _list_with_coord = [2, 0]
#                 return _list_with_coord
#             elif choice_num == 3:
#                 _crest_list[2][2] = 'X'
#                 _list_with_coord = [2, 2]
#                 return _list_with_coord
#             elif choice_num == 4:
#                 _crest_list[1][1] = 'X'
#                 _list_with_coord = [1, 1] 
#                 return _list_with_coord          
#         else: 
#             if choice_num == 0 and _crest_list[0][0] != 'X':
#                 _crest_list[0][0] = 'O'
#                 _list_with_coord = [0, 0]
#                 return _list_with_coord
#             elif choice_num == 1 and _crest_list[0][2] != 'X':
#                 _crest_list[0][2] = 'O'
#                 _list_with_coord = [0, 2]
#                 return _list_with_coord
#             elif choice_num == 2 and _crest_list[2][0] != 'X':
#                 _crest_list[2][0] = 'O'
#                 _list_with_coord = [2, 0]
#                 return _list_with_coord
#             elif choice_num == 3 and _crest_list[2][2] != 'X':
#                 _crest_list[2][2] = 'O'
#                 _list_with_coord = [2, 2]
#                 return _list_with_coord
#             elif choice_num == 4 and _crest_list[1][1] != 'X':
#                 _crest_list[1][1] = 'O'
#                 _list_with_coord = [1, 1] 
#                 return _list_with_coord
#     _list_with_coord = []
#     print(_list_with_coord)
#     if _bot_element == 'X':
#         list_with_coord = generate_choices(_bot_element)
#     elif _bot_element == 'O':
#         list_with_coord = generate_choices(_bot_element)




# crest_list = [[None,None,None],
#               [None,None,None],
#               [None,None,None]]
# gererate_bot_position(crest_list)
# # bot_element = 'X'