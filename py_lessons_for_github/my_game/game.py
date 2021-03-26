import random                                                #random ishlashi
b = 3                                                             #joni
while True:
    a = (random.randint (0,1))                                     #uyin sonlari random tanlash
    print (a,'=')                                                #ekranga chiqarish
    x = int (input ('='))                                           #uynavotgan odami son kiritishi
    if x == a:                                                    #tekshirib olish tengmi yoqmi
        b = b - 1                                                   #agar teng bolsa jondan 1ta olib tashiydi
        if b == 0:                                                #tugatishi tekshirish
            break                                               #tugatish
    if x > 1:                                                     #boshqa sonlar ishtirok etishini tekshirish
        break                                                #tugatish

'''import random                                               #random ishlashi

li = ['+','*','-']                                              #lislardan amallari
jon_sonni = 3                                                   #uyin uchun jon
yutuq = 0                                                       #yutuqlarni xisoblash
soat_hisobi = 0                                                 #soat hisoblash uchun uzgaruvchi

while True:

    birinchi_son = (random.randint(1,10))                       # birinchi son random tanlash
    ikkinchi_son = (random.randint(1,10))                       #birinchi son random tanlash
    amallar = (random.randint(1, len(li)-1))                    #amali random tanlash
    ifdagi_ammalar = li[amallar]                                #litdagi amalni bitta uzgaruvchiga tenglab olish
                                                                #if kampyuter uzi uchun xisob olvoti
    if ifdagi_ammalar == '+':                                   # amal qaysligini bilish
        amal = birinchi_son + ikkinchi_son                        # qushuv amali bolsa ishlash
    elif ifdagi_ammalar == '*':                                 # amal qaysligini bilish
        amal = birinchi_son * ikkinchi_son                        # kupaytruv amali bolsa ishlash
    elif ifdagi_ammalar == '-':                                 # amal qaysligini bilish
        amal = birinchi_son - ikkinchi_son                        # ayiruv amali bolsa ishlash

    print (birinchi_son , li[amallar] , ikkinchi_son ,'=')            #ekranga chiqariash
    javob = int (input('='))                                       #javobni qabul qilib olish

    if amal == javob:                                           #berilgan javob bilan berilgan savolni solishtrish
        yutuq += 1                                              #agar tugri bulsa  tugri javoblar sonini yana bittaga oshiradi
    if amal != javob:                                           #berilgan javob bilan berilgan savolni solishtrish
        jon_sonni -= 1                                          #agar savol notugri bulsa uyindagi jodan bittasini olib tashiydi
        print ('sizning joninggiz',jon_sonni,'ta qoldi')         #qolgan jonlar sonini ekranga chiqaradi
    if jon_sonni == 0:                                          #joni sonini tekshirish
        print ('\n\tuyin tugadi!')                                   #uyin tugaganini habar berish
        print ('siz',yutuq,'ta savolga tugri javob berdiz')      #nechta savolga javob berganini kursatish
        break        '''                                          #uyini tugadish


# windows 7 sapyor uynash
# tekinter interfeyz un
# pygam