reagent = input("Введите название реактива: ")
amount = int(input("Введите количество: "))
with open("inventory.txt", "w", encoding="utf-8") as inventory:
 inventory.write (f"Реактив {reagent} поступил на склад в количестве {amount} шт." )
