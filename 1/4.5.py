# 1 вариант
import math

def calculate_z1(alpha):
    # Переводим градусы в радианы, если alpha задан в градусах
    alpha_rad = math.radians(alpha)
    # Вычисляем z1 согласно формуле
    numerator = 2 * math.cos(alpha_rad) * math.sin(2 * alpha_rad) - math.sin(alpha_rad)
    denominator = math.cos(alpha_rad) - 2 * math.sin(alpha_rad) * math.sin(2 * alpha_rad)
    z1 = numerator / denominator
    return z1

def calculate_z2(alpha):
    # Переводим градусы в радианы, если alpha задан в градусах
    alpha_rad = math.radians(alpha)
    # Вычисляем z2 согласно формуле
    z2 = math.tan(3 * alpha_rad)
    return z2

# Проверка функций для заданного значения alpha (например, 45 градусов)
alpha_test = 45
z1_test = calculate_z1(alpha_test)
z2_test = calculate_z2(alpha_test)

print(f"z1 for alpha={alpha_test} degrees is: {z1_test}")
print(f"z2 for alpha={alpha_test} degrees is: {z2_test}")