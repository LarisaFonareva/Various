x, n = input().split()
for step in range(1, int(n)):
    a = ''
    while x:
        i = 0
        while i < len(x) and x[i] == x[0]:
            i += 1
        a = a + str(i) + x[0]
        x = x[i:]
    x = a
print(a)

# a=input().split()
# for i in range(int(a[1])-1):
#     l,m,s,k='',[],'',-1
#     for x in a[0]:
#         if x==s: m[k]+=1
#         else: l+=x; k+=1; m.append(1)
#         s=x
#     a[0]=''
#     for i in range(len(l)): a[0]+=(str(m[i])+l[i])
# print(a[0])