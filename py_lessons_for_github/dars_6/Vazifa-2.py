#Topshiriq
# 2. 3 ta list yaratish:
#     1-list: 2000 dan kichki Fibonachchi sonlaridan iborat;
#     2-list: 2000 dan kichki Fibonachchi sonlarining faqat toq sonlaridan iborat;
#     3-list: 2000 dan kichik Fibonachchi sonlarining faqat juft sonlaridan iborat bo'lsin.

x = []
y = []
z = []
firstNumber = 0
secondNumber = 1
summ = 0

while firstNumber < 2000:
    x.append(firstNumber)
    summ = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = summ
    if (firstNumber % 2 == 0 and firstNumber) < 2000:
        y.append(firstNumber)
    if (firstNumber % 2 != 0 and firstNumber) < 2000:
        z.append(firstNumber)
print('Fibonachi sonlari: ', x)
print('Juft sonlari: ', y)
print('Toq sonlari: ', z)