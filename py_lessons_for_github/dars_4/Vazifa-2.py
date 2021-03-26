# Topshiriqlar:
# 
# 2. n raqamni kiritish va 0 dan n gacha bo'lgan butun sonlar orasidagi barcha tub sonlarni topish.

# n = int(input('n uchun ixtiyoriy raqam kiriting: '))
# for n in range(0,n):
#     if n%2==0:
#         continue
#     if n%2!=0:
#         print(n)

n = int(input('n uchun ixtiyoriy raqam kiriting: '))

for i in range(1, n):

    i_tub_son = True
    
    for j in range(2, i):
 # i 1 bo'lganda i_tub_son true bo'ladi
 # ...
 # i 3 bo'lganda i_tub_son true bo'ladi
 # i 4 bo'lganda i % j == 0 sharti bajarilib i_tub_son false bo'ladi va 4 ekranga chiqmaydi   
        if i % j == 0:
    
            i_tub_son = False
    
    if i_tub_son:
    
        print(i)