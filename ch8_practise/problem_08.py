'''
write a python function to print muoltiplication table of the a given number 
'''
def multiply(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
    return "done"
print(multiply(5))        