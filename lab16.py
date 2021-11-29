# Write a Python program to remove newline characters from a file.

def remove_newlines(fname):
    line = open(fname).readlines()
    return [s.rstrip('\n') for s in line]

print(remove_newlines("content.txt"))