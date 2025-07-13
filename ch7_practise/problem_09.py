'''
write a program to print the following star patter
***
* *
***
'''
n = int(input("enter the number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*", end="")                     # left border star
        print(" " * (n - 2), end="")            # middle spaces
        print("*")                              # right border star
