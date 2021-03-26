# li = [i for i in range(1,100) if i % 7 == 0]
# print(li)


# def func(li,n):
#     li2 = [i for i in li if i < n]
#     return li2
#
#
# li = [1,2,3,4,5,6,7,8,9]
# x = func(li,3)
#
# print(x)

def func(li):
    return [i**2 for i in li]

li = [2,3,4,5,6,7,8,9]
print(func(li))