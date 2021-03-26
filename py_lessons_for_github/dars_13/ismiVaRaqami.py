# # 2. Ism va telefon raqamni faylga yozib boradigan funksiya yarating.
#
# # Har safar unga ism va raqam yuborilganda faylni davomiga yozib borsin.
#
# # Shu ism va raqamlarni o'qish funksiyasini yozing. Har ikkala funksiya bitta kodda joylashsin.


#
# def read_file():
#     with open('saqlovchi_fayl.txt', 'r') as readeer:
#         see_info = readeer.readlines()
#         return see_info
# print(read_file())
#
# # """Kiritilgan harf katta yoki kichkina bo'lishidan qat'iy nazar harflarni kichkina qilib olish uchun"""
# # while True:
# #     ask = input("Ma'lumotlaringizni kiritish uchun 'Y' ni kiriting, Ko'rish uchun 'K' ni: ")
# #     ask.lower()
# #     if ask == 'Y' or 'y':
# #         print(faylga_yozish())
# #     elif ask == 'K' or 'k':
# #         # read_file()
# #         print(read_file())
# #     else:
# #         print(False)

# def write_to_file():
#     with open('saqlovchi_fayl.txt', 'a') as writer:
#         info = {
#             'Ismi': 'ILYOS',
#             'Raqami': 7871
#         }
#
#         yoz = (str(info) + '\n')
#         writer.write(yoz)
# write_to_file()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def faylga_yozish():
    with open('saqlovchi_fayl.txt','a') as saqlovchi:
        user_info = {
            'ismi': input('Ismingiz: '),
            'raqami': int(input('Telefon raqamingiz: '))
            # 'ismi': 'Ilyos',
            # 'raqami': '7871'
        }
        matn = (str(user_info) + '\n')
        # print(saqlovchi.write(matn))
        saqlovchi.write(matn)
# faylga_yozish()

def read_file():
    with open('saqlovchi_fayl.txt', 'r') as reader:
        info_read = reader.readlines()
        for i in info_read:
            print(i, end='')
        # print(info_read)
# read_file()

def ikkita_func():
    while True:
        ask = input("Ma'lumotlaringizni kiritish uchun 'Y' ni kiriting, Ko'rish uchun 'K' ni: ")
        # ask.lower()
        if ask == 'Y' or ask == 'y':
            print(faylga_yozish())
            # return write_to_file()
            # return faylga_yozish()
        elif ask == 'K' or ask == 'k':
            # return read_file()
            print(read_file())
        # else:
        #     print(False)
ikkita_func()