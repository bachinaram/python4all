def worker1_func():
    global attendence
    attendence=20
    print("this is worker1 function inside block", attendence)

def worker2_func():
    local_var=20
    print("this is worker2 function inside block", attendence, local_var)

def age_func():
    global age
    age=10
    #without assignment it will give you error above assignment is required
    age=age+20
    print("my age in func block is",age)

worker1_func()
worker2_func()
print("outside function",attendence)
age=10
age_func()
print(age)



