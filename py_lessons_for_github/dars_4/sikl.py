#""" for ... in """
# for i in range(10):
#     print('i = ',i)

# for i in range(30):
#     if i>10 and i<20:
#         continue
#     if i % 2 == 0:
#         print(i)

for i in range(30):
    if i % 2 == 0 and ((i>0 and i<11) or (i>20 and i<30)):
        print(i)

