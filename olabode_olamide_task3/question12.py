#12# Ask the user for a sentence and print each word on a new line.
# Step 1: Take input from the user
# Step 2: Split the sentence into words
# Step 3: Print each word on a new line
sentence = input("Enter a sentence: ")
words = "\n".join(sentence.split())
print("Words in the sentence:\n", words)