import random
def token():
    your_token = random.randint(100000000, 200000000)
    return your_token
print(token())
def sonlar(x, y):
    # x = int(input("x = "))
    # y = int(input("y = "))
    if x > y:
        return x
    else:
        return y
# print(sonlar(25,26))