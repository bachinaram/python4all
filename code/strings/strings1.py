'''
h  e  l  l  o     s  t  u  d  e   n   t   s
0  1  2  3  4  5  6  7  8  9  10  11  12  13

 h   e   l   l   o        s   t   u   d   e   n   t   s
-14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   

'''

msg="hello students"
print(msg)
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])

print(msg[0:])
print(msg[1:])
print(msg[2:])
print(msg[3:])

print(msg[0:10])
print(msg[1:10])
print(msg[2:10])
print(msg[3:10])

print(msg[0:10:1])
print(msg[1:10:2])
print(msg[2:10:3])
print(msg[3:10:4])

print(msg[-1])
print(msg[-2])
print(msg[-3])

print(msg[-1:]) #this is same as print(msg[-1])
print(msg[-2:])
print(msg[-3:])

print(msg[-1:-2]) #this wont work
print(msg[-2:-3]) #this wont work
print(msg[-5:-2]) #this will work
print(msg[-2:1]) #this wont work
print(msg[-2:4]) #this wont work
print(msg[-2:13]) #this will work


print(msg[0:-10])
print(msg[1:-10])
print(msg[2:-10])
print(msg[3:-10])


print(msg[::])
print(msg[::1])
print(msg[::-1])

print(msg[0::-1])
print(msg[1::-1]) #start is e from here reverse is eh
print(msg[2::-1]) #start is l from here reverse is leh
print(msg[3::-1]) #start is l from here reverse is lleh

print(msg[0:4:-1]) #wont work
print(msg[1:4:-1]) #wont work
print(msg[1:0:-1]) #start is e from here reverse is eh but end is 0 hence e
print(msg[2:0:-1]) #start is l from here reverse is leh but end is 0 hence el
print(msg[3:0:-1]) #start is l from here reverse is lleh but end is 0 hence ell


print(msg[-1:4:-1])
print(msg[-1:-4:-1])
print(msg[-4:0:-1]) 
print(msg[-4:-1:-1]) #wont work 

