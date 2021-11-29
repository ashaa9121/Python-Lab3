# Program to combine each line from first file with the corresponding line in second file.

with open("file1.txt") as f1:
    with open("file2.txt") as f2:
        for line1,line2 in zip(f1,f2):
            print("Combined files : ",line1 +" "+ line2)