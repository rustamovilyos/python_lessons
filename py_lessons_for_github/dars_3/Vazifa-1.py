# Topshiriq:

# 1. Kiritilgan textda nechta unli harflar borligini aniqlash dasturini yozing.

unli = input("Ixtiyoriy Matn kiriting: ")
unli = unli.lower()
if unli.count('a') or unli.count('e') or unli.count('i') or unli.count('o') or unli.count('u') or unli.count("o'"):

# Barcha unli harflarni .count orqali sanab keyin ularni 1ta o'zgaruvcha tenglab qo'shib olamiz yoki birdaniga printni o'zida chop etamiz
    
    umumiy = unli.count('a') + unli.count('e') + unli.count('i') + unli.count('o') + unli.count('u') + unli.count('o\'')
    print('Siz kiritgan matndagi unli harflar soni: ', umumiy)
elif unli.count('y'):
    print('Bu dastur o\'zbek tilidagi unli harflar sonini hisoblash uchun Y harfi ingliz tilida bazi hollardagina unli harf sifatida ishlatiladi!')
else:
    print('Siz undosh harflardan iborat matn kiritdingiz!')
