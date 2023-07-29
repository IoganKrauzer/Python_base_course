x: int = "Привет "
y: int = " мир "
# print(x + y)

def summa(x1, x2):
    print(x1 + x2)

def summa2(x1: int, x2: int) -> int:
    res: int = x1 + x2
    return res


summa(8,12)
print(summa2(7,13))
print(summa2(" hello ", " world "))