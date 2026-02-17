capsuls = int(input("Введите общее количество произведенных капсул:"))
one_pack = int(input("Введите количество капсул в одной упаковке:"))
full_packs = capsuls // one_pack
rest = capsuls % one_pack
print(f"--- Отчет фасовочного цеха ---\n Полных упаковок:\t {full_packs}\n Остаток капсул:\t {rest}")