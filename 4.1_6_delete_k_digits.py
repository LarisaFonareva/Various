n, k = input(), int(input())
def delete(n, k):
    if k==0:
        return int(n)
    else:
        num = min([n[:i] + n[i+1:] for i in range(len(n))])
        if k > 1:
            return delete(num, k-1)
        else:
            return int(num)
print(delete(n, k))