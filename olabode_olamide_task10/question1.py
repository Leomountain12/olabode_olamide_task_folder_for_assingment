# SIMULATED USSD MENU INTERACTION WITH ERROR HANDLING

try:
    welcom_m = input("Dear valued customer, you are welcome to USSD banking service.\n\tKindly dial *123# to proceed: ")

    if welcom_m == "*123#":
        try:
            menu = int(input("You are welcome. Kindly choose an option.\n\t1. Check your balance.\n\t2. Buy airtime.\n\t3. Buy data.\n: "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            menu = 0
    else:
        print("Invalid input. Please dial *123#")
        menu = 0

    # --- OPTION 1: Check balance ---
    if menu == 1:
        pa = input("Kindly input your password: ")
        pss = "leo1"
        balance = 50000.00

        if pa == pss:
            print(f"Dear valued customer, your available balance is ₦{balance}")
        else:
            print("Invalid password. Try again later.")
            try:
                pas = int(input("Kindly press 1 if you forgot your password: "))
            except ValueError:
                pas = 0

            if pas == 1:
                try:
                    number = int(input("Kindly input the number you used to register your bank account: "))
                except ValueError:
                    number = 0

                if number == 8126332866:
                    number1 = input("Kindly enter your new password: ")
                    print("Dear valued customer, you have successfully changed your password.")
                    pa = input("Kindly input your new password: ")

                    if pa == number1:
                        try:
                            menu = int(input("You are welcome. Kindly choose an option.\n\t1. Check your balance.\n\t2. Buy airtime.\n\t3. Buy data.\n\t0. Back to menu: "))
                        except ValueError:
                            menu = 0

                        if menu == 1:
                            pa = input("Kindly input your password: ")
                            if pa == number1:
                                print(f"Dear valued customer, your available balance is ₦{balance}")
                            else:
                                print("Invalid password. Try again later.")
                else:
                    print("Invalid number. Try again later.")

    # --- OPTION 2: Buy airtime ---
    elif menu == 2:
        price = input("Kindly input your PIN: ")
        pa = "leo1"
        try:
            am = float(input("Kindly enter the amount: "))
        except ValueError:
            am = 0

        if price == pa:
            print(f"Dear valued customer, your ₦{am} airtime purchase was successful. Dial *123# to rollover.")
        else:
            print("Invalid input. Try again later.")

    # --- OPTION 3: Buy data ---
    elif menu == 3:
        price = input("Kindly input your PIN: ")
        pa = "leo1"
        try:
            am = float(input("Kindly enter the amount: "))
        except ValueError:
            am = 0

        if price == pa:
            print(f"Dear valued customer, your ₦{am} data purchase was successful. Dial *123# to rollover.")
        else:
            print("Invalid input. Try again later.")

    else:
        print("Transaction closed. Try again later.")

except (KeyboardInterrupt, EOFError):
    print("\nSession ended. Thank you for using our USSD service.")
