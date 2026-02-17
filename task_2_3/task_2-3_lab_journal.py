fio = input("Введите ФИО")
date = input("Ведите дату")
experiment = input("Введите название эксперимента")
with open("journal.txt", "w", encoding="utf-8")as journal:
journal.write(f"Электронный лабораторный журнал\n ФИО исследователя :\t {fio}\n Дата :\t {date}\n Эксперимент  :\t {experiment}\n Вывод:\n В ходе эксперимента выявлены нарушения долговременной памяти у экспериментальной группы животных")