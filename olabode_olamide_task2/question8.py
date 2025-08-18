
#transport fare calculator
#task 8
dis = float(input("input the distance"))
fare = float(input("input the fare per km"))
total = dis * fare #using the code to calculate amount of t fare
v = f"{total:.2f}" #using the code to put is in 2 decimal place
print(F"your distance is=\t\t{dis}\nyourtranspot fare per km is =\t{fare}\nt0tal t fare=\t\t\t{v}\nThanks") #using f_string to print the result
