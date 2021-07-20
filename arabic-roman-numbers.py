n,result =int(input()), ''
for arabic, roman in zip([1000,900,500,400,100,  90,  50,40,  10,  9,   5,  4,  1],
                         ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']):
    result+=roman*(n//arabic)
    n%=arabic
print(result)