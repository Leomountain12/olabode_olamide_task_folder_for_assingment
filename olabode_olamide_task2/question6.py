#electricity bill formatter
#task 6
name = input("kindly input your name")
unit = int(input("input the unit consume per (kwh)"))
cost = float(input (" input the cost per unit")) #using the float code so that the output can have decimal point
total = unit * cost #using the code to calculate the amount of unit consume and cost per unit
print(f"Dear {name},here is your electric bill.\nunit consume(kwh)=\t{unit}\ncost per unit=\t\t{cost}\ntotal bill=\t\t{total}\nTHANKS")
