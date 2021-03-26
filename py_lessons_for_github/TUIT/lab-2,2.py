n = int(input('n = '))
m = int(input('m = '))
summ = 0
for i in range(n,m+1):
    summ += i**2
    n = summ
print(summ)