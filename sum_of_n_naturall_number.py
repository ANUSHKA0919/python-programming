a=int(input("Enter any number:"))
if a<=0:
    print("Not a natural number")
else:
    sum = 0
    while(a>0):
        sum+=a
        a-=1
    print("the sum is",sum)    
