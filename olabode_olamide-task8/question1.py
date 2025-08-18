#**Task1**
# Explain each output of the program below.
# Give 3 usecases or cenarios where you can apply the program below.
# Write the code for 1 of the 3 use cases.
num1 = int(input("Enter first number: ")) #using integer to ensure the user enter number not letter
num2 = int(input("Enter second number: "))#using integer to ensure the user enter number not letter
#posible output :number1=50 :number2 = 100
print(f"{num1} == {num2} : {num1 == num2}")
#output number1=50  ,number2=100
#explanation
#since number 1 is lesser than number 2, the number one is not equal to number 2.Therefore its false
print(f"{num1} != {num2} : {num1 != num2}") #using f string to print the result
#explanation
#output 
#number1=50 ,number2=100
#since number 1 is lesser than number 2, the number one is not equal to number2.therefore its true
print(f"{num1} > {num2} : {num1 > num2}")
#explanation
#output number1=50 ,number2=100
#since number 1 is lesser than number 2, the number two is greater  than number1.therefore its false
print(f"{num1} < {num2} : {num1 < num2}")
#explanation
# #number1=50 ,number2=100
#since number 1 is lesser than number 2, the number one is lesser than number2.therefore its false



#use cases where it can be used
# to check eligible status
#to confirm student score
# to grade student if they pass or not

#for eligible
age = 16
score = 80
#must be above 18 and score must be above 60
eligible = (age > 18) and (score >60)
print("Scholarship Eligible" ,eligible)
#for student score
cut_off_mark = 70
student_1=40
student_2=80
student_3 = 59
student_4 = 76
print(cut_off_mark >=student_1)
print(cut_off_mark >=student_2)
print(cut_off_mark >=student_3)
print(cut_off_mark >=student_4)
