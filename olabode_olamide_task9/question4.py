#
# 
word = input("Dear userskindly input awords")
print(f"words :{len(word)}")
if word.isupper():
    print('the words is all uppercase')
elif word.islower():
    print("the word is all lowercase")
elif word.istitle():
    print("The word is in title case.")       
else:
    print("The word is a mix of cases or does not fit standard casing rules.")
reversed_word = word[::-1]
print(f"Reversed word: {reversed_word}")