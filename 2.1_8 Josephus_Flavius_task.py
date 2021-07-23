# n,k = int(input()), int(input())
# res = 0
# for i in range(1, n+1):
#   res = (res + k) % i
# print(res + 1)

def joseph(n, k):
    return 1 if n == 1 else (joseph(n - 1, k) + k - 1) % n + 1

print(joseph(int(input()), int(input())))