# Write a Python program to write a list to a file.

languages = ["python","java","php","js"]

with open("content.txt","w") as f:
    for i in languages:
        #print(i)
        f.write("%s\n" %i)

with open("content.txt","r") as f:
    print(f.read())        