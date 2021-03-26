# 4. Yuborilgan listdagi takrorlanmagan elementlarni list ko'rinishida qaytaradigan function yarating.
# Masalan: [2, 3, 5, 3, 2, 6, 7] listi yuborilsa funksiya [5, 6, 7] listini qaytarsin.

def elementlar():
    while True:
        txt = input('Satr kiriting: ')
        printed = []

        for i in txt:
            if (txt.count(i) < 2): #and (i not in printed):
                printed.append(i)
    # print(printed)
        return printed
        
print(elementlar())
