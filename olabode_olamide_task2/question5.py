#daily market report ask the user to input
#task 5
market = input("Dear customer you are welcome to daily market report input. press \"proceed\" to continue:")
name = input("input the name of the market:")
number = int(input("input number of traders"))
rev = float(input("input daily revenue"))
revcom = f"{rev:,}" #using the code for thousand commas
print(f"The name of the market is {name},\n The number of traders is {number},\nDaily revenue generated is #{revcom}. ") #using f string to print the result
