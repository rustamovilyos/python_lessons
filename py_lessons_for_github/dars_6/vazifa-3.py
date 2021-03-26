# Topshiriq
# 3. Raqamlar kiritishni so'rash va kiritilgan raqamlarning toq yoki juft sonligiga qarab 2 guruhga bo'lish.
# 0 raqami kiritilganda raqam kiritishni to'xtatish va har ikkala guruhni ekranga chiqarish.


# birinchi yechim   ILYOS

toq = []
juft = []

from itertools import count
for i in count(1):
    n = int(input('List uchun raqam kiriting: '))
    if n % 2 == 0 and n != 0:
        juft.append(n)
    if n % 2 != 0:
        toq.append(n)
    if n == 0:
        break
print('Toq sonli list: ', toq)
print('Juft sonli list: ', juft)



# # ikkinchi yechim     Adxam aka
# x = int(input('Raqam kiriting: '))
# juft_sonlar = []
# toq_sonlar = []

# while x != 0:
#     if x % 2 == 0:
#         juft_sonlar.append(x)
#     else:
#         toq_sonlar.append(x)

#     x = int(input('Keyingi raqamni kiriting: ')) # x while x != 0 gacha bajarilaveradi
# print('Siz 0 kiritdingiz!')
# print('Juft sonlar: ', juft_sonlar)
# print('Toq sonlar: ', toq_sonlar)