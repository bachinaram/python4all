#error in second line 
cust="customer1"
my_age=int(input("Hello {}, Please confirm your age:".format(cust)))

print("way1")
#indented block in if can not only contain tab space but also any space
if my_age<18:
  print("you are minor, you have no entry. Visit us after {} years".format(18-my_age))
  print("testing")
else:
    print('hello {}, please come in'.format(cust))