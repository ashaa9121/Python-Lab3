# Write a Python program to read a file line by line store it into a variable.

var1 = " "

with open("content.txt","r") as f:
    for line in (f.readlines()):
        #print(line)
        var1  += line  #stored in varible var1

print(var1)        