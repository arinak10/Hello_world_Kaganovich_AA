N = int(input("Введите N: "))
a = float(input("Введите число 1: "))
max_value = a
i = 2
while i <= N:
    a = float(input(f"Введите число {i}: "))
    if a > max_value:
        max_value = a
    i = i + 1
print("Максимальное число:", max_value)