#code block and indentation example
i=10
j=10
str1="hello"
str2="hello"

print("Normal level or Level 0 indentation")
if str1==str2:
    print("level 1 code block start with new indentation")
    if i==j:
        print("level 2 code block start with new indentation")
        j=20
        str2="students"
        print("{0}, {1} today's student count increased from {2} to {3}".format(str1,str2,i,j))
        print("indentation completed for level 2 code block")
    print("Back to level 1")
    print("indentation completed for level 1 code block")
print("Back to Normal level or level 0")
        
