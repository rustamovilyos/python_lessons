# 1. Ikkita satr yuborilsa har ikkala satrda ham mavjud bugan elementlarni qaytaradigan funksiya yarating.
# Masalan: "abcde" va "defjgij" yuborilsa "de" ni qaytarsin.
def bir_xil_matn():
    birinchi_matn = input('1-matnni kirit: ')
    ikkinchi_matn = input('2-matnni kirit: ')
    bir_xillar = []
    for i in birinchi_matn:
        if i in ikkinchi_matn:
            bir_xillar.append(i)
            print(bir_xillar)
bir_xil_matn()