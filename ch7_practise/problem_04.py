n = int(input("enter the number :"))
for i in range(1,n+1):
    if (n%1==0):
        print(f"{n} is not prime")
        break
    else:
        print(f"{n} is prime")