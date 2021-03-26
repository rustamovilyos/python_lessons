# 4. 1 dan 1000 gacha bo'lgan sonlar uchun shunday dictionary yaratingki.
# bunda 1 dan 1000 gacha bo'lgan sonlar kalit (key) ularning kvadrati qiymat (value) bo'lsin.

di = {}
li = []
for i in range(1000):
    li.append(i*i)
    di[i] = li[i]
print(di)