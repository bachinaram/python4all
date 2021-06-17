
number1=int(input("Please enter some number:"))
if number1%2==0:
    print("{} is divisible by 2".format(number1))
elif number1%3==0:
    print("{} is divisible by 3".format(number1))
else:
    print("{} is neither divisible by 2 nor 3".format(number1))


gender=input("please enter your gender:")
gender = gender.lower()
if gender == "male":
    print("You have entered: "+gender)
elif gender == "female":
    print("You have entered: "+gender)
else:
    print("You have entered: "+gender)

