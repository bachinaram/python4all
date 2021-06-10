#implicit conversion example
my_initial_marks=80
my_corrected_marks=4.45
actual_score=my_initial_marks+my_corrected_marks
print(actual_score)

#explicit
result="10"
final_result=10+int(result)
print(final_result)
'''
result1=input("enter your age")
final_result1=10+int(result1)
print("you real age is ",final_result1)
'''
result3=10
print("my age is "+ str(result3))

#hex fucntion converts innt to hexa decimal
print(hex(55))

#convert from int to binary
print(bin(22))

#convert char to unicode, only one char at a time
print(ord('&'))
print(ord('9'))

#convert int to unicode code character, only one int at a time
print(chr(33))
print(chr(57))

# any positive or negative inte,float, complex give to boolit give true
#If 0 are proved then it returns false
print(bool(10))
print(bool(0.0))
