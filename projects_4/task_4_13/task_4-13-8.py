N = int(input("Введите количество элементов N: "))
count = 0
for i in range(1, N + 1):
    ai = float(input(f"Введите элемент {i}: "))
    if ai > 0:
        count = count + 1
print("Количество положительных чисел:", count)