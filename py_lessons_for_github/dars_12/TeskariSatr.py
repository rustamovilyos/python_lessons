# # 1.  Yuborilgan satrni teskari qilib qaytaradigan FUNCTION yarating.
# # Masalan: 'abcdef' yuborilsa 'fedcba' qaytarsin.
#
# def reverse_text(txt :str):
#     ''' ::-1 matnni teskari yozib beruvchi komanda '''
#     return(txt[::-1])
# print(reverse_text('ILyos'))
#
#
#
#
# """Foydalanuvchidan matn so'rab oluvchi function"""
#
# def reverse_text():
#
#     ''' ::-1 matnni teskari yozib beruvchi komanda '''
#
#     txt = input('Matn kiriting: ')
#
#     return(txt[::-1])
#
# print(reverse_text())

###################### 3 ###################
# def reverse_while_loop(s):
#     s1 = ''
#     length = len(s) - 1
#     while length >= 0:
#         s1 = s1 + s[length]
#         length = length - 1
#     return s1
# print(reverse_while_loop('Good'))



# def teskariMatn(text):
#     result = ""
#     for i in text:
#         result = i + result
#     return result
# print(teskariMatn('Teskari yozuv'))