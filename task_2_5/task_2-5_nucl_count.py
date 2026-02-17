dna=input("Введите последовательность ДНК: ").upper()
count_A= dna.count("A")
count_T= dna.count("T")
count_G= dna.count("G")
count_C= dna.count("C")
length=len(dna)
percent_A=(count_A/length)*100
percent_T=(count_T/length)*100
percent_G=(count_G/length)*100
percent_C=(count_C/length)*100
print("Подсчет нуклеотидов: ")
print(f"A: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}")
print(f"Общая длина: {length} нуклеотидов")
print("Процентное содержание каждого нуклеотида:")
print(f"A: {percent_A}\nT: {percent_T}\nG: {percent_G}\nC: {percent_C}")