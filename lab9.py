# Write a Python program to count the number of lines in a text file.

count = 0
with open("content.txt","r") as f:
    for line in f:
        count = count + 1

print("Number of lines : ",count)
       
