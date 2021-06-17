
''' show this error example
my_value=10
for i in my_value:
    print(i)
'''

name="Gaurav"
for eachChar in name:
    print(eachChar)

for eachChar in name:
    print(eachChar.capitalize(), end="")
print()


#overwriting newline backslash with space in using end=" "
for eachChar in name:
    print(eachChar,end=" ")
print()

student1_details=["gaurav",25, 80.0, "80%"]
for eachElement in student1_details:
    print(eachElement)
print()


for eachValue in range(10):
    print(eachValue, end=",")
print()

#increments value by defaults with 1 from 5 to 10
for eachValue in range(5,10):
    print(eachValue, end=",")
print()

#increments value by 2 from range between 1 to 10
for eachValue in range(1,10,2):
    print(eachValue,end="-")
print()

#this prints index
for eachValue in range(len(student1_details)):
    print(eachValue)
    
#using dict we can print keys
my_dict={"name":"Gaurav", "age":20, "marks":50}
for eachKey in my_dict:
    print(eachKey)

for eachValue in (10.5,201.123,91.2):
    print(eachValue,end=",")
print()


#sum of all numbers in list
_gaurav_score=[98,40,45,86,77,57]
total_score=0
for _eachSubjectScore in _gaurav_score:
    total_score=total_score+_eachSubjectScore
print("Gaurav your total is",total_score)
#403/6
print("your percentage is",total_score/(len(_gaurav_score)))

my_list=[[1,2,3],[4,5,6],[7,8,9]]
for eachList in my_list:
    print(eachList)

#nested for   
for eachList in my_list:
    print(eachList)
    for eachValue in eachList:
        print(eachValue)

#list comprehensions

my_list = [i*5 for i in range(2,6)]
for j in my_list:
    print(j,end=',')
print()


my_list2 = [i*5 for i in range(2,6) if (x%2==0)]
print(my_list2) 
#2 table
for i in range(1,11):
    print("540 * {} =".format(i),540*i)

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()



'*' *

'*' *
'*' *

'*' *
'*' *
'*' *

'*' *
'*' *
'*' *
'*' *

'*' *
'*' *
'*' *
'*' *
'*' *