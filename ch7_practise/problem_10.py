'''
write a program to print multiplication table of n in reverse order using for loop .

'''

n = int(input("enter the number :"))
for i in range (1, 11):
    print(f"{n} x {11-i} = {(11-i) * n}")