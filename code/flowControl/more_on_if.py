#print 10 to 100 and print 100 to 10
for j in range(10,110,10):
    print(j)
print()   
for i in range(100,0,-10):
    print(i)
print()

for newj in range(10,110,10):
    if newj == 100:
        print(newj," - front benchers")
    elif newj >= 80:
        print(newj," - friends of front benchers")
    elif newj > 40 and newj < 80:
        print(newj," - Most successful people in life")
    else:
        print(newj," - you must find your different")

#factorial program
"""
10 = 1*2*3*4*5*6*7*8*9*10
0 = 1
1 = 1
-anynumber = not possible"""

fact_number=int(input("enter your factorial number:"))
#for fa in range(1,11):
output=1
if fact_number < 0:
    print("factorial not possible for number {}".format(fact_number))
elif fact_number == 0 and fact_number == 1:
    print("facotrial of number {} is 1".format(fact_number))
else:
    for fa in range(1,fact_number+1):
        output=fa*output
    print(output)

#cube sum
#1**3 + 2**3 + 3**3 + 4**3 + 5**3 = 225
result=0
cube_number=int(input("enter your cube number:"))
for num in range(1,cube_number+1):
    result=(num**3)+result
print(result)