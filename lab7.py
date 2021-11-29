# Write a Python program to read a file line by line store it into an array.

new_array = []

def read_file(x):
    with open(x,"r") as f:
        for line in (f.readlines()):
            #print(line)
            new_array.append(line)

read_file("content.txt")


for x in new_array:
    print(x)

