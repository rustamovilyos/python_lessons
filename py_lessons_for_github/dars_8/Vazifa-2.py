# li = [1,2,34,5,4]


# 2. Satr kiritishni so'rash. Kiritilgan satrda eng ko'p takrorlangan 3 ta element uchun dictionary tuzishю
# Bunda dictionary ni kaliti elementni o'zi, value (qiymati) uni satrda nechi marta takrorlanganligi bo'lishi kerak.
# Masalan: 
# satr: "a bb ccc dddd eeeee ffffff"
# dictionary: {'d': 4, 'e': 5, 'f': 6}

txt = input('Satr kiriting: ')
dic = {}
li = []
top_value = [0, 0, 0]

for i in txt:
    dic[i] = txt.count(i)
print(dic)

li = list(dic.values())

top_value[0] = li.pop(li.index(max(li)))
top_value[1] = li.pop(li.index(max(li)))
top_value[2] = li.pop(li.index(max(li)))

dic.clear()
for i in txt:
    elemetnlar_soni = txt.count(i)
    if elemetnlar_soni in top_value:
        dic[i] = elemetnlar_soni

print(dic)