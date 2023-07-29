# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах




def max_num() -> int:
    max_number: int = 0
    while True:
        n: int = int(input("Введите число: "))
        if n == 0:
            break
        if n > max_number:
            max_number = n
    return max_number
print(f"Максимальное значение  {max_num()} ")






# n : int = int(input("Enter a number > 0: "))
# def Check(n: int) -> bool:
#     is_good = False
#     while n > 0:
#         if n % 10 == 0:
#             is_good = True
#             break
#         n = n // 10
#     return is_good

# def competite(number: int) -> list:
#     temp =[]
#     temp.append(number)
#     while not Check(number):
#         number = int(input("Try again!: "))
#         temp.append(number)
#         if Check(number):
#             print("You win")
#     return temp

# numbers_list = competite(n)
# print(f"Max of entered numbers is: {max(numbers_list)}")