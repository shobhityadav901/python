p1="make a lot money"
p2="buy now"
p3="subscribe now"
p4="click this"

massage=input("Enter your massage: ")
if p1 in massage or p2 in massage or p3 in massage or p4 in massage:
    print("This is a spam message")
else:
    print("This is not a spam message")