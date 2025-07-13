''' WAP to print following star pattern 
*
**  #n=3
*** '''
n= int(input("enter the number :"))
for i in range (1,n+1):
    print("*" * i,end=" ")
    print(" ")