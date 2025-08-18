#9 Ask the user to enter a sentence and print the number of vowels in it.
# Step 1: Take input from the user
# Step 2: Count the vowels
word = input("Enter a sentence: ")
sentence = word.lower()
print("You have", sentence.count("a") + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u'), "vowels in the sentence." )
