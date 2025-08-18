#**Task4: Student Record**
# Create an empty dictionary called student.

# Ask the user to input their name and age, then store them in the dictionary.

# Add a list of scores (e.g., [70, 85, 90]) to the dictionary.

# Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

# Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".

# Print out the complete record in this format:

#Student Record:
#Name: John
#Age: 16
#Scores: [70, 85, 90]
#Passed: True
#Teenager: True

s = {}
s["name"] = input("hello kindly enter your name:")
s["age"] = int(input("enter your age:"))
s["score"] =[60, 70, 80, 90]
avg_sc = sum(s["score"]) / len(s["score"])
s["pass"] = avg_sc >= 50
s["teenager"] = s["age"] >= 13 and s["age"] <=19
print("name:", s["name"])
print("age:",s["age"])
print("score:",s["score"])
print("pass:",s["pass"])
print("teenager:",s["teenager"])

