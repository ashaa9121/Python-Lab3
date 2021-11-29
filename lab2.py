# Write a Python program to read first n lines of a file.

number_of_lines = int(input("Enter no: of lines you want to read: "))
f = open("content.txt")

for i in range(number_of_lines):
    print(f.readline())