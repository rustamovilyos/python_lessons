# user = {'ismi' : 'ILYOS',
#         'yoshi' : 23,
#         'yashash joyi' : 'Sergeli',
#         'jinsi' : 'Erkak',
#         'ma\'lumoti' : 'O\'rta'}

# user['ismi'] = 'Ilyos'
# print(user['ismi'])

# 2
# user = {'ismi' : input('ismingiz: '),

#         'yoshi' : int(input('yoshingiz: ')),

#         'yashash joyi' : input('manzilingiz: '),

#         'jinsi' : input('jinsingiz: '),

#         'ma\'lumoti' : input('ma\'lumotingiz: ')}

# print(user)


# 3

# raqamlar = { 0 : 'nol',
#              1 : 'bir',
#              2 : 'ikki',
#              3 : 'uch',
#              4 : 'to\'rt',
#              5 : 'besh',
#              6 : 'olti',
#              7 : 'yetti',
#              8 : 'sakkiz',
#              9 : 'to\'qqiz',
# }

# print(raqamlar)


# 4 
# di = {'ismi' : 'John',
#       'yoshi' : 35}
# print(di)
# di.update({'familiyasi' : 'Abramov',
#           'Yashash joyi' : 'Toshkent',
#           'yoshi' : 50})
# print(di)

# for kaliti, qiymati in di.items():
# # for kaliti in di:
# # for qiymati in di.values():
#     print(kaliti, ' = ', qiymati)

ди = {'ismi': '', 'familiyasi': ''}
li = ['ILYOS', 'RUSTAMOV']
for i in ди:
    for z in range(2):
        ди[i] = li[z]
print(ди)
