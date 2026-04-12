N = int(input("Введите количество элементов N: "))
sum_ = 0
for i in range(1, N + 1):
    ai = float(input(f"Введите элемент {i}: "))
    sum_ = sum_ + ai
cp = sum_ / N
print("Среднее арифметическое:", cp)