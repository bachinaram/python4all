statement1 = "this is python programming class"
statement2 = "THIS IS PYTHON PROGRAMMING CLASS"
statement3 = "this is python programming class"
statement4 = "thIs Is pyThon progrAMminG class"

print(statement1.upper())       #converts case to upper case
print(statement2.lower())       #converts case to lower case
print(statement1.lower())       #converts case to lower case
print(statement4.capitalize())  #converts sentence to first chat to upper and remaining all to small
print(statement4.swapcase())    #converts all capital letter to small and small letter to Capital

if statement1 == statement4:
    print("both statements are same")
else:
    print("both statements are different")

#how to make sure both sentenance same irrespective of cases
if statement1.upper() == statement4.upper():
    print("both statements are same")
else:
    print("both statements are different")

#split
message="hello, students"
print("message is", type(message))
my_list=message.split(',')
print("my_list is", type(my_list))
print(message.split(','))






