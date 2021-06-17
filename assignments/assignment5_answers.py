print("***********Homework1***********")
#write a program to show list of lists in to individual lists
#e.g., [["ram", 10],["Gaurav", 70],["Lakshmi", 72],["Verma", 81]]
#output 
# ["ram", 10]
#["Gaurav", 70]
#["Lakshmi", 72]
#["Verma", 81]
student_marks=[["ram", 10],
["Gaurav", 70],
["Lakshmi", 72],
["Verma", 81]]

for lst in student_marks:
    print(lst)

    
print("***********Homework2***********")
#write a program to display list of lists in to 
# single line output which should show all values in single line
#e.g., [["ram", 10],["Gaurav", 70],["Lakshmi", 72],["Verma", 81]]
#e.g., output "ram", 10,"Gaurav", 70,"Lakshmi", 72,"Verma", 81
my_string=''
for li in student_marks:
    for val in li:
        print(val, end=' ')
print()


print("***********Homework3***********")
#eligibility check program
#write a program to take int as inputs for 4 subjects and based on input scores
#if any subject score of user is less than 0 then print "please try prelims again"
#else if user's subject score doesnot contain 0 and at least one subject more than 100 print "over acheiver and moved to next level"
#else your subjects doesnt contain any less than 0 or over 100 print "You are eligible"


#create 4 subject variables like science,math,gk,rl
#use input function and give score to each subject
#e.g., science=int(input("enter your science score: "))
#create list and assign all subjects to list
#e.g., my_score=[science,math,gk,rl]
#and also create 3 boolean variables high=False, low=False, medium=False
#use for loop to loop through all subject scores in my_score
#use if condition as mentioned below
#if eachscore in my_score list is greater than or equal to 100 the assign True to high variable
#else if eachscore in my_score list is less than 0 then assign True to low variable
#else assign True to medium variable

#finally come out of for loop and write another if elif and else
#if low is True then print ("please try prelims again")
#elif high is True then print "over acheiver and moved to next level"
#else print "You are eligible "


science=int(input("enter your science score: "))
math=int(input("enter your math score: "))
gk=int(input("enter your GK score: "))
rl=int(input("enter your regional language score: "))
high=False
low=False
medium=False
my_scores = [science,math,gk,rl]
for score in my_scores:
    if score >= 100:
        high=True
    elif score < 0:
        low=True
    else:
        medium=True

if low:
    print("please try prelims again")
elif high:
    print("over acheiver and moved to next level")
else:
    print("You are eligible ")
        
