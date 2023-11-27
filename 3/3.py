# 1 вариант
import random

# Функция для заполнения кортежей
def fill_tuples(n):
    tuple1 = tuple(random.randint(0, n) for _ in range(10))
    tuple2 = tuple(random.randint(-n, 0) for _ in range(10))
    return tuple1, tuple2

# Заполнение кортежей
n = 100  # Максимальное значение n
tuple1, tuple2 = fill_tuples(n)

# Объединение кортежей
tuple3 = tuple1 + tuple2

# Подсчет количества нулей в третьем кортеже
count_of_zeros = tuple3.count(0)

# Вывод третьего кортежа и количества нулей
print("Третий кортеж:", tuple3)
print("Количество нулей в третьем кортеже:", count_of_zeros)