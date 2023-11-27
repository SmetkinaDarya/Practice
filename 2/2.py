# 1 вариант
import random

# Генерация случайного трехзначного кода
correct_code = str(random.randint(100, 999))

# Количество попыток
attempts = 5

# Цикл для попыток отгадать код
for i in range(attempts):
    guess = input(f"Попытка {i + 1}/{attempts}: Введите трехзначный код: ")

    # Проверка, совпадает ли введенный код с верным
    if guess == correct_code:
        print("Вы угадали код! Дверь открыта.")
        break
    else:
        print("Неверный код. Попробуйте еще раз.")

# Если попытки исчерпаны
else:
    print("Попыток больше нет. Дверь заблокирована.")