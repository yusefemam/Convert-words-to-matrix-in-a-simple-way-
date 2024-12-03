import re

text = input("Enter a text: ").strip()
matrix = [[word] for word in re.findall(r'\b\w+\b', text.lower())]
print("Text Matrix:")
for row in matrix:
    print(row)
