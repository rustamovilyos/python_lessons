# Topshiriqlar:
#
# 1. Fibonachchi sonlari ichidan 10 ta tub son toping.
#

def fibo_soni():
    fib_list = [0,1]
    decada = ''
    de = []
    while (fib_list[-1]+fib_list[-2]) < 5000:
        fib_list.append(fib_list[-1]+fib_list[-2])
    for i in fib_list:
        decada = i
        print(decada)
    print(fib_list)
    # for i in fib_list:
    #     if fib_list % i == 0
        # for fib in fib_list:
            # print(decada)
            #     print(f'{fib} soni tub son emas')
            # print(f'{fib} soni tub son')
fibo_soni()


def tub_sonmi(x):
    for i in range(2, x):
        if x % i == 0:
            return (f'{x} soni tub son emas')
        return (f'{x} soni tub son')
    # print('Tub son')
# print(tub_sonmi(6))

# result = tekshir(tub_sonmi,fibo_soni)
# print(result)
