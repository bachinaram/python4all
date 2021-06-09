my_name="student1"
print(my_name)
my_age=20
print(my_age)

#student1="Gaurav"
#student2="Gaurav"
#student3="Gaurav"
#instead of assigning same data to all e variables I used below optimized approach
student1=student2=student3="Gaurav"
print(student1,student2,student3)

#my_real_age=22
#my_real_name="tripati"
#my_real_score=80
#instead of assigning same data to all e variables I used below optimized approach
my_real_age,my_real_name,my_real_score=22,"tripati",80
print(my_real_age,my_real_name,my_real_score)
print(my_real_score)


father_age=my_age+my_real_age
print(father_age)
