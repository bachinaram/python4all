#homework1
person1="Virat"
person2="Sachin"
virat_money=100
sachin_money=150
if (virat_money > sachin_money):
    print("{} is Rich".format(person1))
elif (sachin_money > virat_money):
    print("{} is Rich".format(person2))
else:
    print("Both {} and {} are Rich".format(person1,person2))
    
#homework2
print("{} is Rich".format(person2)) if sachin_money > virat_money else print("{} is Rich".format(person1))
