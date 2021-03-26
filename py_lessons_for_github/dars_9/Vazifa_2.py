def faktorial():
    while True:
        n = int(input('Faktorial: '))
        c = 0
        for i in range(1,n):
            c = n * i
            n = c
        print(c)
faktorial()