# 4. Shunday function yaratingki u foydalanuvchidan raqam kiritishni so'rasin.
# Agar foydalanuvchi raqam kiritishda xatoga yo'l qo'ysa (harf yoki boshqa belgilar kiritsa)
# toki to'g'ri raqam kiritmaguncha qayta qayta so'rasin.
# Agar to'g'ri raqam kiritilsa ushbu raqamni return qilsin.
def raqamKiritish():
    n = input('Raqam kiriting: ')
    # for i in n:
    while True:
        if n.isdigit():
            return n
            # break
        else:
            x = input('Raqam kiriting: ')
        # print(raqamKiritish(5))
    
        # print(n)
print(raqamKiritish())