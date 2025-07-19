'''
snake ,water and gun game
'''
import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,1,0])
youStr = input("enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
you = youDict[youStr]
#by now we have 2 number (variable),you and computer.
print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")
if(computer==you):
    print("its a draw!")
else:
    if(computer==1 and you==-1):
        print("you lose!")
    elif(computer==-1 and you==0):
        print("you lose!")
    elif(computer==0 and you==1):
        print("you lose!")
    elif(computer==0 and you==-1):
        print("you lose!")
    elif(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you lose!")
    else:
        print("something went wrong")