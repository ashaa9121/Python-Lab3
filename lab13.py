# Write a Python program to copy the contents of a file to another file.

with open("file1.txt") as file1:
    with open("file2.txt","w") as file2:
        for line in file1:
            file2.write(line) 

with open("file2.txt","r") as read_file:
    print(read_file.read())