#nigeria currency converter
#task 11
naira = float(input("input the amount in naira (₦):") )
usd = float(input("input  the exchange rate in us dollars($) to naira:"))
pond = float (input ("input the exchange rate in british pounds(£)to naiara:"))
usds  = naira/usd
ponds = naira/pond
usdst =f"{usds:,}"
pondst = f"{ponds:,}"
print(f"therefore  exchange rate  of us dollar in naira=${usdst}\nexchange rate from britich ponds to naira = £{pondst}:")
# simulated ussd menu info