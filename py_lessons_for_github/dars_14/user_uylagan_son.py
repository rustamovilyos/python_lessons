# 3. Foydalanuvchi o'ylagan sonni topish dasturini yozing. Foydalanuvchi 100 dan kichkina 1 ta son o'ylaydi,
# dastur shu sonni topsin.

# Agar kompyuter etgan son to'g'ri bumasa foydalanuvchi o'zi o'ylagan son kompyuter etgan sondan katta
# yoki kichikligini etishi kerak.

# import random
# def comp_number():
#     random_number = random.randint(0,100)
#     while True:
#         if int(input('Please enter number: ')) < random_number:
#             print(int(input(f'agian but this time bigger: ')))
#         elif int(input('Please enter number: ')) > random_number:
#             print(int(input(f'agian but this time smaller: ')))
#         elif int(input('Please enter number: ')) == random_number:
#             print(f'Congratulation you finded the random number:{random_number}')
#         print("You win!")
#         break
# comp_number()
import random
def user_random_numb():
    try:
        random_numb = int(input("Enter your random number: "))
        B = ''
        while True:
            if random.randint(1,100) > random_numb:
                print(random.randint(1,100))
                print("Bigger      Smaller")
                print(B == input('Your number is: '))
                if B == 'Bigger' or B == 'bigger':
                    print(random.randint(1, 100) > random_numb)
                    print("Bigger      Smaller")
                    print(B == input('Your number is: '))
                elif B == 'Smaller' or B == 'smaller':
                    print(random.randint(1, 100) < random_numb)
                    print("Bigger      Smaller")
                    print(B == input('Your number is: '))
            elif random.randint(1, 100) < random_numb:
                print(random.randint(1, 100) < random_numb)
                print("Bigger      Smaller")
                print(B == input('Your number is: '))
                if B == 'Bigger' or B == 'bigger':
                    print(random.randint(1, 100) < random_numb)
                    print("Bigger      Smaller")
                    print(B == input('Your number is: '))
                elif B == 'smaller' or B == 'Smaller':
                    print(random.randint(1, 100) > random_numb)
                    print("Bigger      Smaller")
                    print(B == input('Your number is: '))
            # elif B == 'Smaller' or B == 'smaller':
            #     print(print(random.randint(1, 100) > random_numb))
            #     print("Bigger      Smaller")
            #     print(input('Your number is: '))
            #     if B == 'Bigger' or B == 'bigger':
            #         print(random.randint(1, 100) > random_numb)
            #         print("Bigger      Smaller")
            #         print(input('Your number is: '))
            else:
                print("I'm fond your random number!")
                print(random_numb)
    except ValueError:
        print('Siz raqam kiritishingiz kerak edi!')
user_random_numb()