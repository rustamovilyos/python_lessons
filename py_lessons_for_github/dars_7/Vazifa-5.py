#5. Satr kiritishni so'rash va kiritilgan satrda bir martadan ko'p ishtirok etgan elementlarni ekranga chiqarish
txt = input('Satr kiriting: ')
printed = []

for i in txt:
    if (txt.count(i) > 1) and (i not in printed):
        print(i)
        printed.append(i)
