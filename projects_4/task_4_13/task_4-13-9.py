N = int(input("Введите количество элементов N: "))
sum_ = 0
for i in range(1, N + 1):
    ai = float(input(f"Введите элемент {i}: "))
    if ai % 2 != 0:
        sum_ = sum_ + ai  
print("Сумма всех нечетных элементов:", sum_)