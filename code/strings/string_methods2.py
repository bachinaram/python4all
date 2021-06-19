statement1 = "this is python programming class"
statement2 = "THIS IS PYTHON PROGRAMMING CLASS"

#isupper() islower() will try to find string is a upper/lower or not by returning True or False
if statement1.islower():
    print(f"""Sentence - "{statement1}" is in lower case""")
else:
    print(f"""Sentence - "{statement1}" is not in lower case""")

if statement1.upper().isupper():
    print(f"""Sentence - "{statement1}" is in upper case""")
else:
    print(f"""Sentence - "{statement1}" is not in upper case""")
    
#isdigit() will try to find string is a digit or not by returning True or False
statement3="200"
if statement3.isdigit():
    print(f'statement3 {statement3} is digit')
else:
    print(f'statement3 {statement3} is not digit')

#startswith
message= "Hello, students"
print(message.startswith('Hell'))
print(message.endswith('ent'))
print(message.endswith('ents'))
