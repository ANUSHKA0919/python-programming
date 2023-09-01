#8
a=int(input("enter first side" ))
b=int(input("enter second side" ))
c=int(input("enter third side" ))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("area",area)
