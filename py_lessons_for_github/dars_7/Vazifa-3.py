# 3 Kiritilgan raqamni kvadratini ekranga chiqarish dasturini tuzing. Dastur to'xtovsiz ishlashi kerak.
# Har safar yangi raqam kiritilganda uni kvadranini ekranga chiqarsin


n = int(input('Raqamni kvadratini xisoblash uchun istalgan raqam kiriting: '))
# print(pow(n,2))
print(n**2)
while n != 0:
    x = int(input('Navbatdagi raqamni kiriting: '))
    print(x**2)
    # print(pow(x,2))
    # if n == 0 or x == 0:
    #     print("Siz nol kiritdingiz!")
    #     break