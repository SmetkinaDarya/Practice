# 1 вариант
# Считываем целое число
number = int(input("Введите целое число: "))

# Вычисляем следующее и предыдущее числа
next_number = number + 1
previous_number = number - 1

# Выводим результаты
print("The next number for the number", number, "is", next_number, end=".\n")
print("The previous number for the number", number, "is", previous_number, end=".\n")