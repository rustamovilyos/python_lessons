# 5. Yuborilgan telefon raqamni rostdan O'zbekistonga tegishli va to'g'ri raqamligini tekshiruvchi funksiya yarating.

def uzb_raqami():
    while True:
        raqam = input('Raqamni tekshirish: ')
        check_list = []
        if len(raqam) == 12:
            for i in raqam:
                check_list.append(int(i))
            if check_list[0] == 9 and check_list[1] == 9 and check_list[2] == 8:
                print("Raqam rostan ham O'zbekiston Respublikasiga tegishli ✔")
            # return check_list
        else:
            print("Raqam O'zbekiston Respublikasiga tegishli emas! ❌")

uzb_raqami()