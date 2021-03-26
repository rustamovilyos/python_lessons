#2. raqam kiritishni so'rash va har safar keyingi raqam kiritilganda barcha kiritilgan raqamlar yig'indisini ekranga chiqarish.
# Raqamlar yig'indisi 100dan oshganda dastur tugallashi kerak.
#

n = int(input('Raqam kiriting: '))
summ = 0
while summ < 100:
    m = int(input('Navbatdagi raqamni kiriting: '))
    summ = m + n
    n = summ
    print(summ)