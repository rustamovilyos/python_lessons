
import random
import time

jon = 3
while True:
    boshlangan_vaqt = time.time()
    amallar = ['+', '-']
    birinchi_son = random.randint(1,3)
    ikkinchi_son = random.randint(1,4)
    uchinchi_son = random.randint(1,3)
    print('\n Boshlangan vaqt: ', int(boshlangan_vaqt - time.time()))
    print(birinchi_son, ' + ', ikkinchi_son, ' - ', uchinchi_son, ' =  ')

    if ((int(input('Natija = ')) == (birinchi_son + ikkinchi_son - uchinchi_son))) and (jon > 0):
        print("✔")
        print(f'Sarflangan vaqt: {int(time.time() - boshlangan_vaqt)} s')
        if (int(time.time() - boshlangan_vaqt)) > 4:
            jon -= 1
            print(f'{jon} ta ❤ qoldi! ')
            if jon == 0:
                print('#TUGADI )')
                break
    else:
        print('❌')
        if ((int(input("Yana bir marta urinib ko'ring: "))) ==
            (birinchi_son + ikkinchi_son - uchinchi_son)) and (jon > 0):
            print("✔")
            print(f'Sarflangan vaqt: {int(time.time() - boshlangan_vaqt)} s')
            if (int(time.time() - boshlangan_vaqt)) > 4:
                jon -=1
                print(f'{jon}ta ❤ qoldi!')
                if jon == 0:
                    print('#TUGADI )')
                    break
