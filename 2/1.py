# 1 вариант
# Ввод размеров отверстия A и B
A = float(input("Введите размер A отверстия: "))
B = float(input("Введите размер B отверстия: "))

# Ввод размеров кирпича x, y, z
x = float(input("Введите размер x кирпича: "))
y = float(input("Введите размер y кирпича: "))
z = float(input("Введите размер z кирпича: "))

# Проверка, пройдет ли кирпич через отверстие
if (x <= A and y <= B) or (x <= B and y <= A) or (x <= A and z <= B) or (x <= B and z <= A) or (y <= A and z <= B) or (y <= B and z <= A):
    print("Кирпич пройдет через отверстие.")
else:
    print("Кирпич не пройдет через отверстие.")