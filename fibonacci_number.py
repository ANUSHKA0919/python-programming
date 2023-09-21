#fibonacci-number
n=int(input("Enter the number"))
a=0
b=1
print(a,b, end=' ')
while n>2:
    c=a+b
    print(c,end=' ')
    a,b=b,a
    n-=1
    
