n=int(input())
a=n//60; b=(n-a*60)//20; c=(n-a*60-b*20)//10; d=(n-a*60-b*20-c*10)//5; f=n-a*60-b*20-c*10-d*5
if f+d*5+c*10+b*20>35: f=0; d=0; c=0; b=0; a+=1
elif f+d*5+c*10>17: f=0; d=0; c=0; b+=1
elif f+d*5>8: f=0; d=0; c+=1
print(f,d,c,b,a)