n = int(input())
l = [[0 for i in range(n)] for i in range(n)]
c = 0
i = 0
j = -1
while c != n**2:
    while j < n - 1 and l[i][j+1] == 0:   # двигаюсь влево
        j += 1
        c += 1
        l[i][j] = c
    while i < n - 1 and l[i+1][j] == 0:   # двигаюсь вниз
       i += 1
       c += 1
       l[i][j] = c
    while j > 0 and l[i][j-1] == 0 :   # двигаюсь вправо
       j -= 1
       c += 1
       l [i][j] = c
    while i > 0 and l[i - 1][j] == 0:   # двигаюсь вверх
       i -= 1
       c += 1
       l[i][j] = c
for c in l:
    print(*c)