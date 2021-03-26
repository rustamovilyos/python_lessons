alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY' \
         'ZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '

def fc_encryption():
    shag = int(input('Ключ шифровки: '))
    sms = input("Сообщение для шифровки: ").upper()
    shifr = ''
    for i in sms:
        mesto = alpha.find(i)
        new_mesto = mesto + shag
        if i in alpha:
            shifr += alpha[new_mesto]
        else:
            shifr += i
    print(shifr)
def decrypt():
    ciphertext = input('Пожалуйста, введите ваше зашифрованное предложение здесь:')
    shift = int(input('Введите значение сдвига: '))
    space = []

    # создать список зашифрованных слов.
    ciphertext = ciphertext.split()

    # создать список для хранения расшифрованных слов.
    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    # соединяйте каждое слово в списке предложений пробелом.
    sentence = ' '.join(sentence)
    print('Ваше зашифрованное сообщение:', sentence)

# decrypt()
# fc_encryption()
while True:
    тип = input("Введите 'Ш' для шифрование, для дешифрование Введите 'Д': ")
    if тип == 'Ш':
        fc_encryption()
    elif тип == 'Д':
        decrypt()
    else:
        print('Вы Введили неуказанных символ: ')