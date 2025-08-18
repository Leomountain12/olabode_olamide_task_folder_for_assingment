#simulated ussd menu interraction
# task 12
print("Dear customer you are welcome to leo bank")
dail = input("kindly dail *123# to proceed:")
print("kindly choose an option .\n\t1.\"check balance\"\n\t2.\"buy aitel\"\n\t3.\"buy data\"")
choose = int(input("kindly choose an option from 1,2,or3"))
if choose==1:
    print("       Thanks for choosen option 1")
    pin = int(input("\tkindly input your pin:"))
    print("Dear customer your account balance is ₦5oo.89.\nif you want to rolever kindly dail *123#,Thanks")
elif choose== 2:
    print("       Thanks for choosen option 2")
    number = int(input("\tkindly input your number"))
    amount = int(input("\tkindly input the amount"))
    pin = int(input("\tkindly input your pin"))
    print(f"Dear customer your {amount} airtime is succesful,dail *123# to relover.Thanks")
elif choose== 3:
    print("        Thanks for choosen option 3")
    number = int(input("\tkindly input your number"))
    amount = int(input("\tkindly input the amount"))
    pin = int(input("\tkindly input your pin"))
    print(f"Dear customer your {amount} data  is succesful,dail *123# to relover.Thanks")


