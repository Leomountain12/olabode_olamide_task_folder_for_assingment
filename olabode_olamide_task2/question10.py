#school fees breakdown
#task 10
name = input("kindly input the name of the school")
fee = int(input("input the tuition fees"))
feed_fees = int(input("input the feeding fee"))
hostel = int(input("input hostel fees"))
total = fee + feed_fees + hostel #using the code to calculate the total amount
print(f"SHOOL=\t{name},\nThe  tuition fess is=\t{fee},\nThe feeding fees is=\t{feed_fees},\nThe hostel fee is=\t{hostel},\nThe total amount is=\t{total}") #usinf f_string to print the receipt

