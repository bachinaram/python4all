
msg="From sender to stephen.marquard@uct.ac.za using \n Hellosp gaurav.kumar@uct.ac.za \n Hellosp gaurav.kumar@uct.ac.za \n"
#homework1
domain_count=0
for eachWord in msg.split(" "):
    pos = eachWord.find('@')
    if pos != -1:
        #print(eachWord[:pos])
        domain_count += 1
print(domain_count)


#homework2
for eachWord in msg.split(" "):
    pos = eachWord.find('@')
    if pos != -1:
        print(eachWord[:pos])

