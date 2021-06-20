msg="From sender to stephen.marquard@uct.ac.za using \n Hellosp gaurav.kumar@uct.ac.za \n Hellosp gaurav.kumar@uct.ac.za \n"

for eachWord in msg.split(" "):
    pos = eachWord.find('@')
    if pos != -1:
        print(eachWord[:pos])
print()


#no of occurences of domain
count=0
for eachWord in msg.split(" "):
    pos = eachWord.find('@')
    if pos != -1:
        #print(eachWord[pos+1:])
        count+=1
print(count)
print()


#to get the full email ids in a string
for eachWord in msg.split(" "):
    if(eachWord.find('@')!= -1):
        print(eachWord)
print()

#split
programming_languages="c,java,python,c#,golan,javascript"
print(programming_languages.split(","))
print(programming_languages.split(",",3)) # no of splits

#strip
comment_line="********************acr nfirst line comment acr nnn********************"
print(comment_line.strip("*"))
print(comment_line.strip("*acrsn "))
print(comment_line.strip("a"))

print(comment_line.lstrip("*"))
print(comment_line.lstrip("*acrsn "))


print(comment_line.rstrip("*"))
print(comment_line.rstrip("*acrsn "))

#find(sub, start, end)
message="hello hai students hello how are doing hello"
print(message.find("hello",0))
print(message.find("hello",1,24))
print(message.find("hello",25))
print(message.find("Gaurav"))
