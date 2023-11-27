# Функция для вывода буквы "H" 2 вариант
def draw_h(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or i == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Задайте размер буквы "H"
n = int(input("Введите размер буквы 'H': "))

# Вызов функции для отрисовки буквы "H"
draw_h(n)