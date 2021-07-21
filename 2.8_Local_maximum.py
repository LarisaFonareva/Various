l=[int(i) for i in iter(input,'0')]
ll=[i for i in range(1,len(l)-1) if l[i-1]<l[i]>l[i+1]]   # индексы локальных максимумов
# print(ll)
r=[abs(ll[i]-ll[i+1]) for i in range(len(ll)-1)]  # расстояния между этими индексами
# print(r)
print(min(r) if r else '0')