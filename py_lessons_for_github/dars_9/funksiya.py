# FUNKSIYA
# 1
# def my_func():

#     print('abs')
#     print('Funksiya ishladi')
#     print('Funksiya tugadi')

# my_func()

# 2
# def ekran():

#     print('erkan()')

# ekran()

# 3
# def my_func(x):
#     print(x)
# my_func('aaa')
# my_func('bbb')
# my_func('ccc')

# 4
# def toq_juft(x):
#     if x % 2 == 0:
#         print('Juft: ',x)
#     else:
#         print('Toq: ', x)
# toq_juft(2)
# toq_juft(5)

# 5
# def arifmetik(a, x, y, z,):
    
#     print(a, (x+y+z)/3)
# arifmetik('Javob: ', 1,2,3)
# arifmetik('O\'rta arifmetigi: ', 4,5,7)

# 6
#####    def yigindi(a,b):         #####
#####        kopaytma = a * b      #####
#####        summa = a + b         #####
#####        return summa          #####
#####        # return kopaytma     #####
#####    x = yigindi(4,6)          #####
    
#####    print(x)                  #####   

# 7
def yigindi(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

print(yigindi(2,4,0))