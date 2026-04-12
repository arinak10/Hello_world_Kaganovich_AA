N = int(input("Введите количество элементов N: "))
sum_ = 0
count = 0
for i in range(1, N + 1):
    ai = float(input(f"Введите элемент {i}: "))
    if i % 2 == 0:  
        sum_ = sum_ + ai
        count = count + 1
if count > 0:
    cp = sum_ / count
    print("Среднее арифметическое элементов с четными индексами:", cp)
else:
    print("Нет элементов с четными индексами")