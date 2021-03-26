a = int(input('a = '))
b = int(input('b = '))

# x = (a**a) + (b**b)
x = pow(a,2) + pow(b,2)
# y = (a + b)**2
y = pow(a+b,2)

if x > y:
    print('x = ', x)
else:
    print('y = ', y)