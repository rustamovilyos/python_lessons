а = int(input('введите число для а: '))
б = int(input('введите число для б: '))
с = int(input('введите число для с: '))
д = int(input('введите число для д: '))

if (а+б)%4 == 0:
    print("а + б")
else:
    print("а + б:", False)
if (б+с)%4 == 0:
    print("с + б")
else:
    print("а + б:", False)
if (с+б+а)%4 == 0:
    print("а + б + с")
else:
    print("а + б + с:", False)
if (д+б+с)%4 == 0:
    print("б + с + д")
else:
    print("б + с + д:", False)
if (а+с+б+д)%4 == 0:
    print("а + б + с + д")
else:
    print("а + б + с + д:", False)