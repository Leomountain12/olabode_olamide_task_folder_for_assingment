#
name = (input("Dear candidate you are welcome to 2025/2026 federal government admission portal,kindly input your name:"))
age  = int(input("kindly input your age "))
if age >= 18:
    score = int(input("kindly input your jamb score:"))
    print(score)
else:
    print("Dear candidate you are not eligible for the admission thanks.")
if score >= 200:
    olevel = (input("Did you have 5credit pass in your o level icluding maths and english?.:"))
    print(olevel)
else:
    print("unable to process your application.")
if olevel == "yes":
    scr = int(input("kindly input your post-utme online screening mark:"))
    print(scr) 
else:
    print("you are not eligible for the 2025/2026 admisssion into federal university thanks.")  
if scr>= 60:
    dpt = int(input("re enter your jamb score:"))
    print(dpt)
else:
    print("Dear candidate we cannot proceed your application thanks.")   
if dpt >= 200:
    print(f"Dear {name} \ncongratulations you have been offrered a provisional addmission into the\n federal unuversity to study english language   thanks. ")     
