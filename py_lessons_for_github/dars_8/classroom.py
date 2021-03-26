# txt = 'aabbdddbfeif'
# print(txt)
# li = list(txt)
# print('txt = ', txt)
# print('li = ', li)

# Matn kiritishni so'rash va matnda faqat 3marta ishtirok etgan harflarni ekranga chiqarish  
txt = input('')

my_li = []

for i in txt:
    if (txt.count(i) == 3) and (i not in my_li):
        print(list(i))
        my_li.append(i)