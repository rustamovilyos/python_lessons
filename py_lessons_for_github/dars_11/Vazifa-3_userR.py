foydalanuvchi = open("userlar.txt", 'r')
foydalanuvchi = foydalanuvchi.readlines()
login = input('Loginingizni kiriting: ')
parol = input('Parolingizni kiriting: ')

if (login == foydalanuvchi['login']) and (parol == foydalanuvchi['parol']):
    print(foydalanuvchi['ismi'])
