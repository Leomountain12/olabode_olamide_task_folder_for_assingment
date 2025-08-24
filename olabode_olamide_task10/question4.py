#
# 
try:
    word = input("Dear user, kindly input a word: ")

    print(f"Number of characters: {len(word)}")

    if word.isupper():
        print("The word is all uppercase.")
    elif word.islower():
        print("The word is all lowercase.")
    elif word.istitle():
        print("The word is in title case.")
    else:
        print("The word is a mix of cases or does not fit standard casing rules.")

    reversed_word = word[::-1]
    print(f"Reversed word: {reversed_word}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
