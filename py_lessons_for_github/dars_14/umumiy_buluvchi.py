# 2. Shunday funksiya yaratingki, unga yuborilgan 2 ta sonning eng katta umumiy bo'luvchisini qaytarsin.
# Yani har ikkala yuborilgan sonni qoldiqsiz buladigan eng katta sonni qaytarsin.
# Agar har ikkala sonni qoldiqsiz buladigan umumiy 1 ta son bumasa 0 qaytarsin.
# Masalan:  75 va 50 uchun 25 ni qaytarsin. 21 va 35 uchun 7ni. 27 va 31 uchun 0 qaytarsin.
def u_b():
    # while True:
    x = int(input('x = '))
    y = int(input('y = '))
    # umumiy_buluvchi = []
    for i in range(x-1,1,-1):
        if x % i == 0 and y % i == 0:
            # umumiy_buluvchi.append(i)
            return i
    return 0
print(u_b())