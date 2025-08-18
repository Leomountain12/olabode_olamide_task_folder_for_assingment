#**Task2**
# Comment the code below appropriately, and using doctring, explain what the code is doing.
# Adapt the code to the case below.
# Federal Government Scholarship Key Eligibility Requirements:
# Citizens
#  Applicant must be a citizen of Nigeria. 
# Enrollment: Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
#  Other Scholarships:
# Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international.  Academic Qualification: For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.
# name = input("Enter your name: ")
# age = int(input("Enter your age: ")) #using int to allow the to imput ordinary number
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70) # using eligible status to check if any student are aligible or not
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
#the output will show which student is eligible or not

#adapt the code to the cases
f = int(input("welcome to federal government scholarship press 1 to proceed:"))
N =input("kindly input your full name:")
cit = int(input("are you a cittizen of nigeria?.\n1.yes\n2.no\nkindly choose from option 1 or 2:"))
enr = int(input("are  a registered, full-time undergraduate student in a recognized Nigerian university?.\n1.yes\n2.no\nkindly choose from option 1 or 2:"))
sch = int(input("are you currently receiving any other scholarship from an entity in the Oil and Gas industry?..\n1.yes\n2.no\nkindly choose from option 1 or 2:"))
qua = int(input("Did you have five distinctions (As and Bs) in relevant subjects in your WAEC/WASSCE (May/June) exams, including English and Mathematics?.\n1.yes\n2.no\nkindly choose from option 1 or 2:"))
#the output will show which student is eligible or not
eligibility = (f==1) and (cit==1) and (enr==1) and (sch==2) and (qua==1)
print(f"Candidate: {N}\nEligible: {eligibility}")