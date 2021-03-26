# 3. 0 dan 10 gacha bo'lgan sonlar ichidan 1000 marta random son tanlang. Olingan random sonlarning qaysi biri nechi marta takrorlanganligini aniqlab ekranga chiqaring.
# masalan:
# 0 raqami: 39 marta
# 1 raqami: 120 marta
# 2 raqami: 184 marta
# 3 raqami: 92 marta
# . . . . 
# . . . .
# . . . .
# 9 raqami: 72 mart1a

import random
result = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}
for i in range(1,1001):
    random_son = random.randint(0,9)
    random_son = str(random_son)
    i = random_son

print(random_son)
# print(i)