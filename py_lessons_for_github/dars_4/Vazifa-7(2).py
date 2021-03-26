# Topshiriq:

# 2. n raqamni kiritish va 0 dan n gacha bo'lgan  sonlar orasidagi barcha oxiri 5 bilan tugaydigan sonlarni topish.
# Masalan: 15, 75, 185 va h.k.

n = int(input('n uchun istalgan raqam kiriting: '))
for besh in range(n):
    if (besh % 5 == 0) and (besh % 2 != 0):
        print(besh)