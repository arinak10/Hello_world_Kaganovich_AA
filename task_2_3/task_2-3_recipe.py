substrate = input("Введите название питательной среды:")
concentration = input("Введите концентрацию агара (%):")
temperature = input("Введите температуру стерилизации (°C):")
with open ("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"Введите название питательной среды:\t {substrate}\n Введите концентрацию агара (%):\t {concentration}\n Введите температуру стерилизации (°C):\t {temperature}\n Файл 'recipe.txt' успешно сформирован!")