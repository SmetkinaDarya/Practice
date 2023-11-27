#1 вариант
import math

# Ввод значения x
x = float(input("Введите значение x: "))

# Вычисление вспомогательного выражения
helper_expression = 2 * x**3 + 6 * x**2 - math.sqrt(x)

# Вычисление модуля
absolute_value = abs(helper_expression)

# Вычисление обратной дроби
reciprocal = 3 / helper_expression

# Вычисление значения y(x)
y_x = absolute_value + reciprocal

# Вывод результата
print("Значение выражения y(x) =", y_x)

# Проверено на примерах:
# X=1 => Y~7,42
# X=2 => Y~38.6
# X=3 => Y~106.2
# X=4 => Y~222
# X=5 => Y~397.7