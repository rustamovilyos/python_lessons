"""     QUIZ #1: Foydalanuvchidan raqam so'rash raqam kiritmaguncha qauyta-qayta so'rayverish.
    Raqam kiritsa raqamni qaytarish   """
# def xatolik():
#     while True:                                            #while orqali so'ralgan narsa bajarilmaguncha so'rayverish
#
#         try:                                               #xatolik turini tekshirish...boshlanishi
#
#             return int(input('Raqam kirit = '))   #kiritilgan ma'lumotni tekshirib natijani qaytarish
#
#         except ValueError:                                 #xatolik turini tekshirish...xatolik turini topish
#
#             print('Raqam kiritsangchi!!!!')                #xatolik turini tekshirish...#TUGADI
#
# print(xatolik())                                           #Funksiyani chaqirib ishlatish

"""     QUIZ #2    """

# def quiz2():
#     while True:
#         li = ['bir', 'ikki', 'uch', "to'rt"]
#         try:
#             print(li[int(input("Raqam kiritib ko'ring: "))-1])
#         except IndexError:
#             return (f'List uzunligi: {len(li)} ')
# print(quiz2())

"""     QUIZ #3    """
try:
    print(x + y)
except NameError:
    print("Siz oldin e'lon qilinmagan o'zgaruvchini ishlatmoqchisiz! ")
