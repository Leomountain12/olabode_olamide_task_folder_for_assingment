#4
request = int(input("Dear customer kindly enter your info.  pres 1 to continue:"))
one = input("input your first name:")
two = int(input("input your age:"))
three = input("input your favourite color:")
four = input("input your home town:")
all = (one,two,three,four)
(one,two,three,four) = all
print(f'{one}\n{two}\n{three}\n{four}')