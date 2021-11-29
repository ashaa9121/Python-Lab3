# Write a Python program to append text to a file and display the text.

def file_append(x):
    with open(x,"a") as f:
        f.write("\nfirst line appended")
        f.write("\nsecond line appended")

file_append("content.txt")

with open("content.txt") as f:
    print(f.read())
    