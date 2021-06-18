
my_list=[[1,2,3],[45,34,89],["sneha","suresh","ankith"]]
long_list = [value for list in my_list for value in list]
print(long_list)

for element in long_list:
  if element == "sneha" or element == "suresh" or element == "ankith":
    print(f"element {element} is a string")
  else:
    print(f"element {element} might be an int")
