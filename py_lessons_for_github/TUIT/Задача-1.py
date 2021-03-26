x = input('Введите число для х: ')
a = 0
while True:
    if x.isdigit():
        x = int(x)
        a = 2*(pow(x,4))-3*(pow(x,3))+4*(pow(x,2))-5*x+6
        print('Значение Полинома = ', a)
        x = input('Введите число для х: ')
    else:
        print(False)
        x = (input('Введите только число = '))
