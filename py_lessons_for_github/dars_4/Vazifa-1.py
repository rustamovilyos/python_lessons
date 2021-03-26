# Topshiriqlar:


# 1. 1400 va 2800 orasidagi barcha ham 7 ga ham 5 ga qoldiqsiz bo'linadigan sonlarni toping.

for i in range(1400, 2800):
    if (i%7!=0 and i%5!=0):
        continue
    if i%7==0 and i%5==0:
        print(i, 'Ham 5ga ham 7ga bo\'linadi!')