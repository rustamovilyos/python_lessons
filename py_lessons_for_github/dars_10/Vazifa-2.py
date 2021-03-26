# 2.Foydalanuvchi "soat" deb yozsa hozirgi soatni,
# "minut" deb yozsa minutni
# "sekund" deb yozsa sekundni ekranga chiqarish dasturini tuzing.

import time

время = {
    'soat' : 'H',
    'minut' : 'M',
    'sekund' : 'S'
     }
     
while True:
        name = input('BlaBlaBla: ')
        if name in время:
            print(time.strftime(f"%{время[name]}"))
        else:
            print('xato')

# x = int(input('x = '))
# y= int(input('y = '))
# print(f'{x} + {y} = {x + y}')


    # h = 'soat'
    # m = 'minut'
    # s = 'sekund'
    # while True:
    #     Soat = input('Soat, minut va sekundlardan birini kiriting: ')
    #     Soat = Soat.lower()
        # if Soat == h:
        #     print(time.strftime('%H'))
        # elif Soat == m:
        #     print(time.strftime('%M'))
        # elif Soat == s:
        #     print(time.strftime('%S'))
        # else:
        #     print("Faqat soat, minut yoki sekundni kiriting!")
        # 






        
        # 
        # soat = input("Hozirgi soatni bilish uchun 'soat' so'zini kiriting: ")
        # soat = soat.lower()
        # if (soat.isalpha) and (soat == h):
        #     # return time.strftime('%H')
        #     print(time.strftime('%H'))
        # else:
        #     soat = input("Hozirgi soatni bilish uchun 'soat' so'zini kiriting: ")
        # minut = input("Hozirgi soatni bilish uchun 'minut' so'zini kiriting: ")
        # minut.lower()
        # if (minut.isalpha) and (minut == m):
        #     # return time.strftime('%M')
        #     print(time.strftime('%M'))
        # else:
        #     minut = input("Hozirgi soatni bilish uchun 'minut' so'zini kiriting: ")
        # sekund = input("Hozirgi soatni bilish uchun 'sekund' so'zini kiriting: ")
        # sekund.lower()
        # if (sekund.isalpha) and (sekund == s):
        #     # return time.strftime('%S')
        #     print(time.strftime('%S'))
        # else:
        #     sekund = input("Hozirgi soatni bilish uchun 'sekund' so'zini kiriting: ")
# vaqt()