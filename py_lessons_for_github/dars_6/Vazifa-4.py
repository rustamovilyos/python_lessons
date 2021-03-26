# 4. Ma'lumotlar kiritishni so'rash. Xech narsa kiritmasdan ENTER tugmasi bosilguncha qiymatlarni qabul qilish.
# Qabul qilingan qiymatlarni "raqamlar" va "satrlar" nomli guruhlarga bo'lish. "raqamlar" guruhiga faqat raqamlardan
# iborat satrlarni jamlash. Qolgan barcha satrlarni "satrlar" nomli guruhga jamlash.


# birinchi_yechim ILYOS

# Raqam = []
# Satr = []

# from itertools import count
# for i in count(1):
#     n = input('Istalgan qiymat kiriting: ')
#     if n.isdigit():
#         Raqam.append(n)
#     elif n.isalpha():
#         Satr.append(n)
#     else:
#         print('Raqam ', Raqam)
#         print('Satr ', Satr)
#         break

# ikkinchi_yechim Adxam aka

# x = input('Ma\'lumot kiriting: ')
# raqamlar = []
# satrlar = []

# while len(x) > 0:
#     if x.isdigit():
#         raqamlar.append(x)
#     else:
#         satrlar.append(x)
    
#     x = input('Keyingi ma\'lumot kiriting: ')

# print('Siz xech qanday ma\'lumot kiritmadingiz!')
# print('raqamlar: ', raqamlar)
# print('satrlar: ', satrlar)