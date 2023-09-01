#6
a=int(input("enter number in seconds"))
h=a//3600
s=a-(h*3600)
m=s//60
t=s-(m*60)
print("hours",h,"minutes",m,"seconds",t)
