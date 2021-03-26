# 4. Yuborilgan raqamni qaysi operatorga tegishli ekanini aniqlovchi funksiya yarating.
# Masalan nomer 998970000000 bo'lsa Mobiuz, 998901112233 bo'lsa Beeline, 998946664455 bo'lsa Ucell va h.k.
def mobil_operatori():
    while True:
        raqam_kiritish = input('Mobil operatoringizni bilish uchun raqamingizni kiriting = ')
        tekshirish = []
        if len(raqam_kiritish) == 12:
            for i in raqam_kiritish:
                tekshirish.append(int(i))
            if tekshirish[4] == 7:
                print('Mobiuz')
            elif tekshirish[4] == 4 or tekshirish[4] == 3:
                print('Ucell')
            elif tekshirish[4] == 0 or tekshirish[4] == 1:
                print('Beeline')
            print(f'Raqamingiz: {raqam_kiritish}')
        else:
            print("Raqam noto'g'ri kiritilgan!")
mobil_operatori()
