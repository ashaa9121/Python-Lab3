# Write a Python program to read a random line from a file.

import random

with open("content.txt","r") as f:
    lines  = f.read().splitlines()
    
print("Random line : " , random.choice(lines))