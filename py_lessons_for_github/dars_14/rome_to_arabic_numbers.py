# 5.Rim raqamalarini yuborilsa arab raqamlari ko'rinishida qaytaradigan funksiya yarating.
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
def int_to_arabic(input):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
        count = (input / nums[i])
        result += nums[i] * count
        input -= ints[i] * count
    return result
print(int_to_arabic(IX))

