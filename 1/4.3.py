# 1 вариант
import math

# Ввод внешнего и внутреннего радиусов
R = float(input("Введите внешний радиус кольца: "))
r = float(input("Введите внутренний радиус кольца: "))

# Вычисление площади кольца
area = math.pi * (R**2 - r**2)

# Вывод результата
print("Площадь кольца: ", area)