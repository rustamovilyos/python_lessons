# Topshiriq:

# 3. Kiritilgan satrda 'a', 'b' va 'c' harflaridan qaysi biri eng ko'p ekanligini aniqlang. Agar ular teng bo'lsa buni ham aniqlang.
# Mison uchun: "satrda eng ko'p harf bu a"
# "satrda a va b harflari soni teng"
x = input("Введите текст: ")
x = x.lower()
if x.count('а') > x.count('б') and x.count('а') > x.count('с'):
    print('Наибольшее количество букв в вашем тексте - A. Их количество:', x.count('а'))
elif  x.count('б') > x.count('а') and x.count('б') > x.count('с'):
    print('Наибольшее количество букв в вашем тексте - Б. Их количество:', x.count('б'))
elif  x.count('с') > x.count('а') and x.count('с') > x.count('б'):
    print('Наибольшее количество букв в вашем тексте - С. Их количество:', x.count('с'))
elif  x.count('б') == x.count('а'):
    print('В вашем тексте количество букв - А и Б. Их количество:', x.count('б'))
elif  x.count('б') == x.count('с'):
    print('В вашем тексте количество букв - Б, С. Их количество:', x.count('б'))
elif  x.count('а') == x.count('с'):
    print('В вашем тексте количество букв - А, С. Их количество:', x.count('а'))
elif  x.count('б') == x.count('а') and x.count('б') == x.count('с') and x.count('а') == x.count('с'):
    print('В вашем тексте количество букв - А, Б, С. Их количество:', x.count('б'))
else:
    print('0')