# 4. Yuborilgan sonni rim raqamlari ko'rinishida qaytaradigan funksiya yarating.'
# Masalan 7 yuborilsa "VII" ni qaytarsin, 15 yuborilsa "XV", 24 yuborilsa "XXIV" va h.k.
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
def int_to_roman(input):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = " "
    for i in range(len(ints)):
        count = int(input / ints[i])
        result += nums[i] * count
        input -= ints[i] * count
    return result
print(int_to_roman(2313))

# def romanize(number):
#    n2rMap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
#    roman = ""
#    for key in n2rMap.keys():
#       count = int(number / key)
#       roman += n2rMap[key] * count
#       number -= key * count
#    return roman
# print(romanize(23))
#
