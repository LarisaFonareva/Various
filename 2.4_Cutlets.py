k, m, n = [int(input()) for _ in 'tri']
# if n<=k:
#   print(2*m)
# elif n*2%k==0:
#   print(m*(n*2//k))
# else:
#   print(m*(1+(n*2//k)))
print(2 * m * (n > 0) if n <= k else m * ((n * 2 % k != 0) + (n * 2 // k)))