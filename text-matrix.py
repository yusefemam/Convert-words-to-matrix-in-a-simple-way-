import re
from collections import Counter

text = input("Enter a text: ").strip().lower()
words = re.findall(r'\b\w+\b', text.lower().strip())

print("Text matrix:")
for _ in words:
    print([_], end = " " *2)

counts = Counter(words)

print("\nWord counts:")
for word, count in counts.items():
    print(f"{word}: {count}")
