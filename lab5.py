# Write a Python program to read a file line by line and store it into a list.

new_list = [] 

with open("content.txt","r") as f:
    for line in (f.readlines()):
        new_list.append(line)

for x in new_list:
    print(x)       