# Описание проекта: требуется написать программу, способную шифровать и дешифровать
# текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).
# def ru_encription(s):
#     for c in s:
#         if c.isupper():
#             if ord(c)+step>1071:
#                 cc=ord(c)+step-32
#             else:
#                 cc = ord(c) + step
#         elif c.islower():
#             if ord(c)+step>1103:
#                 cc=ord(c)+step-32
#             else:
#                 cc = ord(c) + step
#         else:
#             cc=ord(c)
#         print(chr(cc),end='')
# def ru_decription(s):
#     for c in s:
#         if c.isupper():
#             if ord(c) - step < 1040:
#                 cc = ord(c) - step + 32
#             else:
#                 cc = ord(c) - step
#         elif c.islower():
#             if ord(c) - step < 1072:
#                 cc = ord(c) - step + 32
#             else:
#                 cc = ord(c) - step
#         else:
#             cc=ord(c)
#         print(chr(cc),end='')
# def en_encription(s):
#     for c in s:
#         if c.isupper():
#             if ord(c) + step > 90:
#                 cc = ord(c) + step - 26
#             else:
#                 cc = ord(c) + step
#         elif c.islower():
#             if ord(c) + step > 122:
#                 cc = ord(c) + step - 26
#             else:
#                 cc = ord(c) + step
#         else:
#             cc = ord(c)
#         print(chr(cc),end='')
# def en_decription(s):
#     for c in s:
#         if c.isupper():
#             if ord(c) - step < 65:
#                 cc = ord(c) - step + 26
#             else:
#                 cc = ord(c) - step
#         elif c.islower():
#             if ord(c) - step < 97:
#                 cc = ord(c) - step + 26
#             else:
#                 cc = ord(c) - step
#         else:
#             cc = ord(c)
#         print(chr(cc), end='')
#
# direction=input('Будем шифровать или дешифровать текст? ш=шифровать, д=дешифровать: ')
# language=input('Какой язык? р=русский, а=английский: ')
# step=int(input('Задайте шаг сдвига вправо: '))
# a=input('Введите текст: ')
# if direction=='ш':
#     if language=='р':
#         ru_encription(a)
#     else:
#         en_encription(a)
# else:
#     if language=='р':
#         ru_decription(a)
#     else:
#         en_decription(a)

# Текст "Hawnj pk swhg xabkna ukq nqj." был получен в результате шифрования
# алгоритмом Цезаря с сдвигом вправо на nn символов. Расшифруйте данный текст.
# Примечание. Считайте, что n \in [0; \, 25]n∈[0;25].
# def en_decription(s,step):
#     for c in s:
#         if c.isupper():
#             if ord(c) - step < 65:
#                 cc = ord(c) - step + 26
#             else:
#                 cc = ord(c) - step
#         elif c.islower():
#             if ord(c) - step < 97:
#                 cc = ord(c) - step + 26
#             else:
#                 cc = ord(c) - step
#         else:
#             cc = ord(c)
#         print(chr(cc), end='')
#     print()
# a=input('Введите текст: ')
# for i in range(26):
#     print(i)
#     en_decription(a,i)

# На вход программе подается строка текста на английском языке, в которой
# нужно зашифровать все слова. Каждое слово строки следует зашифровать с
# помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.
a=input().split()
encr_a=[]
for c in a:
    step=0
    for j in c:
        if j.isalpha():
            step+=1

    encr_c=''
    for j in c:
        if j.isalpha():
            if j.isupper():
                if ord(j) + step > 90:
                    cc = ord(j) + step - 26
                else:
                    cc = ord(j) + step
            elif j.islower():
                if ord(j) + step > 122:
                    cc = ord(j) + step - 26
                else:
                    cc = ord(j) + step
        else:
            cc = ord(j)
        encr_c+=chr(cc)
    encr_a.append(encr_c)
print(' '.join(encr_a))

# a = input().split()
# abc = 'abcdefghijklmnopqrstuvwxyz'
# ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# encr_a = ''
# for c in a:
#     step = len([i for i in c if i.isalpha()])
#     for i in c:
#         if i in abc:
#             encr_a += abc[(abc.find(i) + step) % 26]
#         elif i in ABC:
#             encr_a += ABC[(ABC.find(i) + step) % 26]
#         else:
#             encr_a += i
#     encr_a += ' '
# print(encr_a)