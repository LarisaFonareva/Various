# x,y=0,0
# while True:
#     try:
#         a=input().split()
#         if a[0] == 'North':
#             y += int(a[1])
#         elif a[0] == 'South':
#             y -= int(a[1])
#         elif a[0] == 'East':
#             x += int(a[1])
#         elif a[0] == 'West':
#             x -= int(a[1])
#     except EOFError:
#         print(x,y)
#         break
# # В Пайчарме после ввода строк надо нажать [Enter] и [Ctrl-D]. Иначе выдаст ошибку.

import sys

x,y=0,0
for i in sys.stdin:
    d, val = i.split()
    if d == 'South':
        y -= int(val)
    elif d == 'North':
        y += int(val)
    elif d == 'West':
        x -= int(val)
    else:
        x += int(val)
print(x, y)
# В Пайчарме после ввода строк надо нажать [Enter] и [Ctrl-D]. Иначе выдаст ошибку.