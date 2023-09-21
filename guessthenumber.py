#guessthenumber
from random import *
n=randrange(1,101)
score=10
while True:
    a=int(input("Enter any Number:"))
    if a==n:
        print("You Win",score)
        break
    elif a<n:
        print("smaller then computer number")
    else:
        print("larger then computer number")
    score-=1    
