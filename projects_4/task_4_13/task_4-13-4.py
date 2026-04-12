N = int(input("Введите N: "))
i = 1
sum_ = 0
while i <= N:
    sum_ = sum_ + i
    i = i + 1
print("Сумма первых", N, "натуральных чисел:", sum_)