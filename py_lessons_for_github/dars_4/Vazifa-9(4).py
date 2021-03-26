# Topshiriq:


# 4. n sonini kiritishni so'rash. Noldan n sonigacha bo'lgan har bir raqamni olib,
#   noldan shu raqamgacha bo'lgan sonlar yig'indisini ekranga chiqaring.

# Masalan:
# n = 6 bo'lsa:
# 0 uchun 0
# 1 uchun 0
# 2 uchun 1 (0+1)
# 3 uchun 3 (0+1+2)
# 4 uchun 6 (0+1+2+3)
# 5 uchun 10 (0+1+2+3+4)

# n = int(input(' '))
# seq = range(n)
# yig = sum(seq)

# print('+'.join(map(str, seq)))
# print("Сумма:", yig)

# end = int(input(''))
# start = 0
# a = start
# s = 0
# while a < end:
#     if a == end:
#         print(end, end='\n')
#     else:
#         print(a, end='+')

#     s += a
#     a = a + 1

# print("Сумма:", s)


n = int(input('n uchun raqam kiriting: '))

for bir in range(n):
    sum = 0
    for i in range(bir):
        sum = sum + i
    print(bir, ': ', sum)
