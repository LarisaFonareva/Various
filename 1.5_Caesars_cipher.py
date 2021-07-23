d=int(input())
for c in input():
    if c.isalpha():
        if c.islower():
            print(chr((ord(c)+d-1072)%32+1072),end='')
        else: print(chr((ord(c)+d-1040)%32+1040), end='')
    else:
        print(c,end='')