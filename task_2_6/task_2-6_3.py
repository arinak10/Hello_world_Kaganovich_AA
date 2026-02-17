donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите фенотип группы крови реципиента(I, II, III, IV): ").strip().upper()
if donor == "I":
    print("возможно")
elif donor == "II" and recipient == "II":
    print("возможно")
elif recipient == "I":
    print("невозможно")
elif donor == "II" and recipient == "III":
    print("невозможно")
elif donor == "II" and recipient == "IV":
    print("возможно")
elif donor == "III" and recipient == "II":
    print("невозможно")
elif donor == "III" and recipient == "III":
    print("возможно")
elif donor == "III" and recipient == "IV":
    print("возможно")
else:
    print("невозможно")