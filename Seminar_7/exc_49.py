# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# 20 минут
# Семинар 7. Функции высшего порядка
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     max_s = 0
#     for i in orbits:
#         ploshad = 3.14*i[0]*i[1]
#         if max_s < ploshad:
#             max_s = ploshad
#     return max_s

# print(find_farthest_orbit(orbits))
# print(*find_farthest_orbit(orbits))


def find_farthest_orbit(orbits):
    S = list(map(lambda item: 3.14*item[0]*item[1] if item[0] != item[1] else 0, orbits))
    return f"Самая далекая планета имеет индекс {S.index(max(S))}"

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))