import time
n=int(input("Enter any number:"))
print("Counter start")
while n:
    print(n)
    n-=1
    time.sleep(1)
else:
    print("counter stop")
