pin=1234
amount=50000
user_pin=int(input("enter the pin number:"))
if user_pin==pin:
    print("1.deposition\n 2.withdrawal\n 3.balance enquiry")
    ch=int(input("enter your choice"))
    if ch==1:
        damount=int(input("enter your amount:"))
        amount=amount+damount
        print("your available balance is",amount)
    elif ch==2:
        wamount=int(input("enter your amount:"))
        amount=amount-wamount
        print("your available amount is",amount) 
    elif ch==3:
        print("your available amount is",amount)      
    else:
        print("wrong input")
else:
    print("invalid pin number")             
