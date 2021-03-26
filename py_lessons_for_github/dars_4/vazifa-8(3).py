# Topshiriq

# 3. a va b raqamlarni kiritishni so'rash. 
# a dan katta va b dan kichkina sonlar orasidan o'zaro yig'indisi b ga teng bo'lgan barcha raqamlarni topish.
# a = int(input('a uchun raqam kiriting: '))
# b = int(input('b uchun raqam kiriting: '))

# for i in range(a,(b+1)):
#     for k in range(i+1):
#         if k + i == b:
#             print('i =', i, 'va k = ', k, 'sonlari yig\'indisi >> ', b)

a = int(input('a uchun raqam kiriting: '))
b = int(input('b uchun raqam kiriting: '))

for i in range(a+1,b):
    for k in range(a+1, b):
        if k + i == b:
            print('i =', i, 'va k = ', k, 'sonlari yig\'indisi >> ', b)