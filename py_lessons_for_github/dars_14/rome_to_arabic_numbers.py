# 5.Rim raqamalarini yuborilsa arab raqamlari ko'rinishida qaytaradigan funksiya yarating.
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
def roman_to_arabic_num(roman_num):
    roman_num = roman_num.upper()
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    arabic_num = 0
    for i in range(len(roman_num)):
        if i > 0 and roman_dict[roman_num[i]] > roman_dict[roman_num[i - 1]]:
            arabic_num += roman_dict[roman_num[i]] - 2 * roman_dict[roman_num[i - 1]]
        else:
            arabic_num += roman_dict[roman_num[i]]
    return arabic_num


print(roman_to_arabic_num('MCMXCIV'))

