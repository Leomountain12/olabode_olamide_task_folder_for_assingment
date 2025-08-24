#
try:
    name = input("Dear candidate you are welcome to 2025/2026 federal government admission portal, kindly input your name: ")
    
    age = int(input("Kindly input your age: "))
    
    if age >= 18:
        try:
            score = int(input("Kindly input your JAMB score: "))
            print(score)
        except ValueError:
            print("Invalid input for JAMB score. Please enter a number.")
            exit()
    else:
        print("Dear candidate, you are not eligible for the admission. Thanks.")
        exit()

    if score >= 200:
        olevel = input("Did you have 5 credit passes in your O-Level including Maths and English? (yes/no): ").strip().lower()
        print(olevel)
    else:
        print("Unable to process your application.")
        exit()

    if olevel == "yes":
        try:
            scr = int(input("Kindly input your Post-UTME online screening mark: "))
            print(scr)
        except ValueError:
            print("Invalid input for screening mark. Please enter a number.")
            exit()
    else:
        print("You are not eligible for the 2025/2026 admission into the federal university. Thanks.")
        exit()

    if scr >= 60:
        try:
            dpt = int(input("Re-enter your JAMB score: "))
            print(dpt)
        except ValueError:
            print("Invalid input for JAMB score. Please enter a number.")
            exit()
    else:
        print("Dear candidate, we cannot proceed with your application. Thanks.")
        exit()

    if dpt >= 200:
        print(f"Dear {name},\nCongratulations! You have been offered a provisional admission into the\nFederal University to study English Language. Thanks.")
    else:
        print("You do not meet the final JAMB score requirement. Thanks.")

except ValueError:
    print("Invalid input. Please make sure to enter numeric values where required.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
