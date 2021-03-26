foydalanuvchilar = open('userlar.txt', 'w')
malumotlar = {'ismi' : input('Ismingiz: '),
              'login' : input('Loginingiz: '),
              'parol' : input('Parolingiz: ')
              }
for i in malumotlar.values():
    foydalanuvchilar.write(str(i) + '\n')