# 1 вариант
import math

class NumberRootDictionary:
    def __init__(self):
        self.dictionary = {}

    def creates(self, n):
        for number in range(1, n + 1):
            root = math.sqrt(number)
            self.dictionary[number] = root

# Создание экземпляра класса
num_root_dict = NumberRootDictionary()

# Вызов метода creates для заполнения словаря
n = 10  # Максимальное число для словаря
num_root_dict.creates(n)

# Вывод заполненного словаря
print(num_root_dict.dictionary)