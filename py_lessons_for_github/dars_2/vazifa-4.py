x = int(input('x ga ixtiyoriy son kiriting:'))
y = int(input('y ga ixtiyoriy son kiriting:'))
print('Siz kiritigan ma\'lumot turi: ', 'x -> ', type(x), 'y ->', type(y))
# print('Siz kiritigan ma\'lumot turi: ', type(y))
print('x + y = ', x+y)
print('x - y = ', x-y)
z = x//y 
print('x ni y ga bo\'lganda bo\'linmaning butun qismini ekranga chiqarish -> x // y = ', z)
t = x%y
print('x ni y ga bo\'lganda bo\'linmaning qoldiq qismini ekranga chiqarish -> x % y = ', t)
m = z + t # uchunchi va to'rtinchi punktlarni yig'indisini olish osonroq bo'lishi uchun ularga alohida o'zgaruvchilar berildi 
print('Butun qism va qoldiq qismning yig\'indisi: ', m)