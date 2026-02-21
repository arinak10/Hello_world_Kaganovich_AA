name = input("Введите имя оператора:")
pressure = input("Введите текущее значение давления (Па):")
with open("sensor_log.txt", "w", encoding="utf-8") as log:
    log.write(f"Введите имя оператора:\t {name}\n Введите текущее значение давления (Па):\t {pressure}\n Данные успешно сохранены в sensor_log.txt")