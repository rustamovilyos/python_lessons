#  5000 dan kichik bo'lgan Fibonachchi sonlari ichidan tasodifiy 3 tasini ekranga chiqaring.
#
import random
fibo = []
x = []
firstNumber = 0
secondNumber = 1
summ = 0

while firstNumber < 5000:
    fibo.append(firstNumber)
    summ = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = summ
# fibo = int(fibo)
ran = random.randint(fibo[0],fibo[-1])
x.append(ran)
# x[0] = fibo.pop(ran)
# x[1] = fibo.pop(ran)
# x[2] = fibo.pop(ran)

print('Fibonachi sonlari: ', fibo )
print(x)

