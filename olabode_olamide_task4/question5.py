# #task 5
# student_names = []
# student_scores = []
# Ask the user to enter three items for their shopping list
item1 = input("Enter the first item for your shopping list: ")
item2 = input("Enter the second item for your shopping list: ")
item3 = input("Enter the third item for your shopping list: ")

# Store the items in a tuple
shopping_list = (item1, item2, item3)

# Convert the tuple to a list
shopping_list_list = list(shopping_list)

# Ask for two more items to add
item4 = input("Enter a fourth item to add: ")
item5 = input("Enter a fifth item to add: ")

# Add the new items to the list
shopping_list_list.append(item4)
shopping_list_list.append(item5)

# Convert the list back to a tuple
shopping_list = tuple(shopping_list_list)

# Print the updated list using join() with " | "
print("\nUpdated Shopping List:")
print(" | ".join(shoppin))