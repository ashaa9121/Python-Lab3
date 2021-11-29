# Write a Python program to get the file size of a plain file.

import os

file_size = os.path.getsize("plain_file.txt")
print()
print("The size of the file is :", file_size,"bytes")