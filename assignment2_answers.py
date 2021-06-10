#assignment2  homework1
student1=input("Enter student name1:")
student2=input("Enter student name2:")
student3=input("Enter student name3:")
print("Student1 Name is:"+student1+"\n"+"Student2 Name is:"+student2+"\n"+"Student3 Name is:"+student3)


#assignment2  homework2
def function1():
    print("Function1 output:",age)

def function2():
    age=30
    print("Function2 output:",age)

def function3():
    global age
    age=40
    print("Function3 output:",age)
age=20
function1()
function2()
function3()
print("Outside function output:",age)
