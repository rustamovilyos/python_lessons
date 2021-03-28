
import random
import time
award = 0
award_time = 0
jon = 3
while True:
    boshlangan_vaqt = time.time()
    birinchi_son = random.randint(1,3)
    ikkinchi_son = random.randint(1,4)
    uchinchi_son = random.randint(1,3)
    print(birinchi_son, ' + ', ikkinchi_son, ' - ', uchinchi_son, ' =  ')

    if ((int(input('Natija = ')) == (birinchi_son + ikkinchi_son - uchinchi_son))) and (jon > 0):
        award = award + 1
        print("✔")
        print(f'Sarflangan vaqt: {int(time.time() - boshlangan_vaqt)} s')
        if (int(time.time() - boshlangan_vaqt)) > 5:
            jon -= 1
            print(f'{jon} ta ❤ qoldi! ')
            if jon == 0:
                print('#TUGADI )')
                print(f"Siz {award} ball to'pladingiz")
                break
    else:
        print('❌')
        ask_again = (int(input("Yana bir marta urinib ko'ring: ")))
        if (ask_again == (birinchi_son + ikkinchi_son - uchinchi_son)) and (jon > 0):
            award = award + 1
            print("✔")
            print(f'Sarflangan vaqt: {int(time.time() - boshlangan_vaqt)} s')
            if (int(time.time() - boshlangan_vaqt)) > 5:
                jon -=1
                print(f'{jon}ta ❤ qoldi!')
                if jon == 0:
                    print('#TUGADI )')
                    print(f"Siz {award} ball to'pladingiz")
                    break
