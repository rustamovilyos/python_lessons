with open("fibo.txt", 'w') as yoz:
    birinchi_son = 0
    ikkinchi_son = 1
    rezerv = 0
    while ((birinchi_son) < 5000):
        # print(birinchi_son)
        rezerv = birinchi_son + ikkinchi_son
        birinchi_son = ikkinchi_son
        ikkinchi_son = rezerv
    # fibo_list = [0,1]
    # while (fibo_list[-2] + fibo_list[-1]) < 10000:
    #     fibo_list.append(fibo_list[-1] + fibo_list[-2])
        yoz.write(str(birinchi_son) + ', ')