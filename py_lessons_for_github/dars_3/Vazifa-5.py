# 5. Kiritiligan yilning kabisa yili ekanligini (fevral oyi 29 kunlik yil kabisa yili) aniqlash dasturini tuzing.
# Ma'lumot: 
# - agar yil 4 ga qoldiqsiz bo'linsa kabisa yili;
# - lekin agar yil 100 ga qoldiqsiz bo'linsa kabisa yili emas;
# - lekin agar yil 400 ga qoldiqsiz bo'linsa baribir kabisa yili.

# Masalan 1600-yil kabisa yili. 1700-yil kabisa yili emas.
x = int(input('Kabisa yilini kiriting: '))

if (x%4 == 0 and x%100 != 0) or (x%400 == 0):
    print('Kabisa yili')
# elif
else:
    print('Kabisa yili emas!')