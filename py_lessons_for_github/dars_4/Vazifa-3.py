# Topshiriqlar:
# 
# 3. Kiritilgan n raqamdan dan kichik bo'lgan va o'zaro ko'paytmasi n ga teng bo'lgan barcha raqamlarni topish.

# n = int(input(' '))

# for i in range(n):
#     i_bir = True
#     for j in range(i):
#         if j * i == n:
#             # print(i)
#             i_bir = False
#     if i_bir:
#         print(i, j)   

n = int(input('n ni kiriting: '))

for i in range(n):
     for j in range(i+1):
         if j * i == n:
             print(i,'va', j, ' sonlari ko\'paytmasi')