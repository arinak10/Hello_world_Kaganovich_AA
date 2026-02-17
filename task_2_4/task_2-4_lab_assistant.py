V = int(input("Введите нужный объем раствора:"))
m_nacl = V * 0.009
v_h2o = V 
with open("receipt.txt", "w", encoding="utf-8") as receipt:
    receipt.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n -----------------------\n Общий объем:\t {V} мл\n Масса соли:\t {m_nacl} г\n Объем воды:\t {v_h2o} мл")