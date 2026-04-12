N = int(input("Введите N: "))
sum_ = 0
for i in range(1, N + 1):
    sum_ = sum_ + i**2
print("Сумма квадратов первых", N, "натуральных чисел:", sum_)