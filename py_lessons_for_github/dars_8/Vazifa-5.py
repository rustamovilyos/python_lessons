# 5. Shunday dictionary yaratingki bunda 1 dan 25 gacha bo'lgan sonlar kalit (key)
# va har bir shu son uchun 0 dan o'zigacha bo'lgan sonlar yig'indisi qiymat (value) bo'lsin.
# Masalan:
# {1: 0, 2: 1, 3: 3, 4: 6, 5: 10 .......}

# di = {}
# li = []
# x = 0
# for i in range(25):
#     x = x + i
#     li.append(x)
#     di[i] = li[i]
# print(di)

dic = {}
for i in range(1,25):
    dic[i] = 0
    for k in range(i):
        dic[i] = dic[i] + k

print(dic)