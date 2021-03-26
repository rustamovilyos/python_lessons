# Topshiriq:

# 2. x ni kiriting;
# - agar x toq son bo'lsa, shu bilan birga 10 dan katta va 18 dan kichik bo'lsa ekranga "to'g'ri" so'zini;
# - agar x juft son bo'lsa va 5 dan katta va 15 dan kichik bo'lsa "noto'g'ri" so'zini;
# - boshqa barcha xollarda "noaniq" so'zini chiqaring.
# Izoh: ekranga faqat bitta so'z chiqishi kerak.

x = int(input('Введите число: '))

if (x % 2 != 0) and (x > 10 and x < 18):
    # в Математике 2*x+1 выражения всегда дает нечетное число
    # в Питоне x % 2 > 0 выражения всегда дает нечетное число
    print("Число которое вы ввели: ", x)
    print('Нечетное число')
    # print("Верно")
elif (x % 2 == 0) and (x > 5 and x < 15):
      # в Математике 2*x выражения всегда дает четное число
      # в Питоне x % 2 == 0 выражения всегда дает четное число
    print("Число которое вы ввели: ", x)
    print('Четное число')
    # print('Неверно')
else:
    print("Число которое вы ввели: ", x)
    print('Неточно')