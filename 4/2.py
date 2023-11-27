# 1 вариант
total_sum = 0

try:
    while True:
        num = float(input("Введите число (или нажмите Ctrl+C для завершения): "))
        total_sum += num
except KeyboardInterrupt:
    print("Вы нажали клавишу прерывания.")
    print("Итоговая сумма:", total_sum)