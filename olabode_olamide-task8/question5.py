#
store = {"benz":30 ,"lexus" :90 , "camry":100}
#item in the sstore
print("Dear value customer ,this are the remaining items that remain in  the store.\n1.benz:30 \n2.lexus :90  \n3.camry:100}")
name = input("Dear customer kindly input your name:")
item = input("kindly enter the item you want to buy:")
item_quality = int(input("how many {item} will you like to purchase:"))
#printing dictionary before purchase
print(f"before purchase: {store}")
store[item] -= item_quality
#printing the dictionary after purchase
print(f"after purchase{store}")