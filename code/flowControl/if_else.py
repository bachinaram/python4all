cust="customer1"
my_age=int(input("Hello {}, Please confirm your age:".format(cust)))

print("way1")
if my_age<18:
    print("you are minor, you have no entry. Visit us after {} years".format(18-my_age))
else:
    print('hello {}, please come in'.format(cust))

print("way2")
if my_age<18:print("you are minor, you have no entry. Visit us after {} years".format(18-my_age))
else:print('hello {}, please come in'.format(cust))

print("way3")
print("you are minor, you have no entry. Visit us after {} years".format(18-my_age)) if my_age < 18 else print('hello {}, please come in'.format(cust))