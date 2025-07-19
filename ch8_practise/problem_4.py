'''
write a recursive function to calculate the sum of first n natural numbers
'''

'''
sum(1)=1
sum(2)=2+1
sum(3)=3+2+1
sum(4)=4+3+2+1
sum(5)=5+4+3+2+1
sum(n)=n+(n-1)+......+5+4+3+2+1
'''


def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)
n = int(input("enter the natural number n: "))
print(f"the sum of {n} natural number is {sum(n)}")
