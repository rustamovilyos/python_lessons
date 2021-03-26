# with open('data.txt', 'r') as reader:
#     line = reader.readline()
#     print(line)

# with open('juft_sonlar.txt', 'a') as juft:
#     for i in range(50):
#         if i % 2 == 0:
#             juft.write(str(i) + '\n')


with open('matnlar.txt', 'a') as matn:
    matnlar = ' '
    while matnlar:
        matnlar = input('Matn kiriting: ')
        matn.write(str(matnlar) + '\n')
# with open('data.txt', 'r') as file:
#     lines = file.readline()
#     # for line in lines:
#     print(lines)

# # st = 'ABCDGFYIK'
# # for i in st:
# #     print(i, end='+')

# # with open('data.txt', 'w') as file:
# #     li = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff']
# #     for st in li:
# #         file.write(st + '\n')

