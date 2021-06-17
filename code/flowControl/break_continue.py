'''for eachChar in "students":
    if eachChar == 'd':
        break
    else:
        print(eachChar)

for eachChar in "students":
    if eachChar == 'd':
        continue
        print(eachChar)
    else:
        print(eachChar)

for eachChar in "students":
    if eachChar == 's':
        continue
    elif eachChar == 'd':
        print(eachChar,end="")
    else:
        print(eachChar,end="")
print()


#sum of positive number only

numbers=[10,-6,7,-2,1,0,-4,9]
output=0
for num in numbers:
    if num < 0:
        continue
    else:
        output+=num
print("sum of positive numbers from the list {0} is {1}".format(numbers,output))

#sum sequence with even numbers only
numbers1=[10,-6,-2,12,0,-4]
output1=0
for num1 in numbers1:
    if num1%2!=0:
        output1=0
        print("Sorry, I can't sum because list has odd number/s")
        break
    else:
        output1+=num1
print(f"Sum of even numbers {output1}")    


my_list=[[1,2,3],[4,5,6],[7,8,9]]

for list in my_list:
    print(list)
    for val in list:
        if val%2==0:
            break
            #continue
        print(val)
'''
my_list2 = [i*5 for i in range(2,6) if (i%2==0)]
print(my_list2)

my_list=[[1,2,3],[4,5,6],[7,8,9]]
my_list3 = [y for x in my_list for y in x]
print(my_list3)