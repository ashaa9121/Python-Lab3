# Write a Python program to count the frequency of words in a file.


counts = {}
with open("content.txt","r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
print()
print("The frequency of words in file :\n")                
print(counts)                    