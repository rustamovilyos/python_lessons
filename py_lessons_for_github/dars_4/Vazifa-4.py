# Topshiriq:
# 4. 1991-yildan 2050-yilgacha bo'lgan oraliqdagi barcha kabisa yillarini aniqlash.

for n in range(1991, 2050):
    if n % 4 != 0:
        continue
    if n % 4 == 0:
        print('Kabisa yili = ', n)