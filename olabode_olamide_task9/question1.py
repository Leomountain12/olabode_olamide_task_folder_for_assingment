#SIMULATED USSD MENU INTERACTION
welcom_m = input("Dear valued customer ,you are welcome to ussd banking service.\n\tkindly dial *123# to proceed:")

if welcom_m == "*123#":
    menu = int(input("you are welcome.kindly choose and option.\n\t1.check your balance.\n\t    2.Buy airtime.\n\t    3.Buy data.: ")) 
else:
    print("invalid input. dail *123#")
if menu == 1:
    pa = input("    kindly input your passward:")
    pss = "leo1"
    balance =50000.00
    if pa == "leo1":
        print(f"Dear valued customer your available balance is.₦{balance}")
    else:
        print("    invalide password try again  later")
        pas = int(input("kindly press 1 to forget your passward:"))
        
        if pas == 1:
            nunber=int(input("kindly put your the number you used to registered your bank:"))
            print(nunber)
        else:
            print("invalide code")
        if nunber == 8126332866:
            number1 = input("kindly enter your new passward:")    
            print(number1)
            print("Dear valued customer you have succeessfully changed your pass ward") 
        else:print("invalid try again later")  
        
        pa = input("    kindly input your passward:")
        if pa == number1:
             menu = int(input("you are welcome.kindly choose and option.\n\t1.check your balance.\n\t    2.Buy airtime.\n\t    3.Buy data.\n\t0.Back to menu: "))
             print(f"{menu}")
             if menu == 1:
                 pa = input("    kindly input your passward:")
                 pa == number1
                 if pa == number1:
                      print(f"Dear valued customer your available balance is.₦{balance}")
                 else:
                     print("    invalide password try again  later")
             
        
            
elif menu == 2:
    price = input("\tkindly input your pin.:")   
    pa = "leo1"
    am = float(input("\tkindly enter the amount.:"))
    if price == pa:
        print(F"Dear valued customer your ₦{am} artime is successful .dail *123# to roleover")
    else :
        print("    invalide input try again  later")
        pas = int(input("kindly press 1 to forget your passward:"))
        
        if pas == 1:
            nunber=int(input("kindly put your the number you used to registered your bank:"))
            print(nunber)
        else:
            print("invalide code")
        if nunber == 8126332866:
            number1 = input("kindly enter your new passward:")    
            print(number1)
            print("Dear valued customer you have succeessfully changed your pass ward") 
        else:print("invalid try again later")  
        
        pa = input("    kindly input your passward:")
        
                
        
elif menu == 3:
    price = input("\tkindly input your pin.:")  
    pa = "leo1"
    am = float(input("\tkindly enter the amount.:"))
    if pa == "leo1":
        print(F"Dear valued customer your ₦{am} data is successful .dail *123# to roleover")
    else :
        print("    invalide input try again  later")
else:
    ("transaction close try agin later")

        



    

          
          

