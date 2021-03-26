# Topshiriqlar:

# 1. 3200 va 4300 orasidagi barcha ham 7 ga ham 9 ga  qoldiqsiz bo'linadigan toq sonlarni toping.

# i = 0
# while (i > 3200) and (i < 4300):
#     i % 7 ==0 and i % 5 == 0 and i % 2 != 0
#     print(i)
for toq_son in range(3200, 4300):
    if toq_son % 7 ==0 and toq_son % 5 == 0 and toq_son % 2 != 0:
        print('3200 va 4300 ga bo\'linuvchi toq son >>', toq_son)