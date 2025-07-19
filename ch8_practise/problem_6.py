'''
write  a python function which  convert inches to cms
'''
def inch_to_cms(inch):
    return inch * 2.54
n = int (input("enter the values of inches: "))
print(f"{n} inches is equal to :{inch_to_cms(n)} cms")