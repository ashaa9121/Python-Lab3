# Write a Python program to read last n lines of a file.

n = int(input("Enter no: of lines : "))

with open("content.txt") as f:
    for line in (f.readlines() [-n:]):
        print(line)