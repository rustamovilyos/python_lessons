# x = [1,2,3,4,5,4,3,2,333,22]
# print(x[3])

# a = '23'
# b = 'ILYOS'
# x = [a, b]
# print(x)

# x = [12, 23, 32, 42]
# print(x)
# x.append(322)
# x.append(300)
# print(x)

# a = [11, 12, 13]
# print(a)
# x = int(input('x uchun son kiriting: '))
# y = int(input('y uchun son kiriting: '))
# z = int(input('z uchun son kiriting: '))

# a.append(x)
# a.append(y)
# a.append(z)

# a = [x,y,z]
# print(a)

#foydalanuvchidan massiv uchun 4ta qiymat so'rash
x = []
for i in range(4):
    x.append(input('Qiymat kirit: '))

print(x)


# a = 'abcd'
# for i in a:
#     print(i)

# sanoq boshidan 100 gacha bo'lgan sonlarni massivga qo'shish:
# a = []

# for i in range(101):
#     if i % 2 == 0:
#         a.append(i)
#         print('juft son: ', a)
#     # else:
#     elif i % 2 != 0:
#         a.append(i)
#         print('Toq son: ', a)
 
#  x = []
# for i in range(101):
#      x.append(i)

# for i in x:
#     if i % 2 != 0:
#         print(i, '>> Juft son')
#     else:
#         print(i, '>> Toq son')

#!!!!!!!!!!!! x = []
# for i in range(3):
#     x.append(input('Qiymat kirit: '))
#     for j in i:
#     print(len(x))

# x = []
# a = input('Qiymat kirit: ')
# b = input('Qiymat kirit: ')
# c = input('Qiymat kirit: ')
# x.append(a)
# x.append(b)
# x.append(c)
# print(x, len(x))
# if (len(a) > len(b)) and (len(a) > len(c)):
#     print('A eng ko\'p: ',len(a), a)
# elif (len(b) > len(a)) and (len(b) > len(c)):
#     print('B eng ko\'p: ',len(b), b)
# elif (len(c) > len(b)) and (len(c) > len(a)):
#     print('C eng ko\'p: ',len(c), c)

# x = []
# for i in range(3):
#     x.append(input('x ga element kirit: '))

# index = 0
# uzunlik = 0
# for i in range(3):
#     if len(x[i]) > uzunlik:
#         index = i
#         uzunlik = len(x[i])
# print(x[index])

# x = [1, 23, 34]
# for i in x:
#     if i > 10:
#         print(i)