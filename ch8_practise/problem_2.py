'''
write a python program using function to convert temperature from Celsius to Fahrenheit
'''


def f_to_c(f):
    return 5*(f - 32)/9


f=int(input("enter the temperature in f :"))
c= f_to_c(f)
print(f"{round(c,2)} degree celsius")