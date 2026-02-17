weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (cм): "))
bmi = weight / (height ** 2)
print(f"--- Отчет о состоянии здоровья ---\n Рост:\t {height}\n Вес:\t {weight}\n Индекс массы тела:\t {bmi}")