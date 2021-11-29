# Write a Python program to remove newline characters from a file.

def content_without_newline(file_1):
	content = ''
	with open(file_1, 'r') as f1:
		content = f1.read()
	with open(file_1, 'w') as f1:
		f1.write(content.replace('\n', ''))
	with open(file_1, 'r') as f1:
		print("contents without new line characters\n")
		print(f1.read())

content_without_newline('content.txt')