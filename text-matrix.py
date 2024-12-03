import re
from collections import Counter

print("Welcome to Linguistics engineering 🫶! ")
text = input("Enter a text: ").strip().lower()
words = re.findall(r'\b\w+\b', text)

print("\nText matrix:")
for i, word in enumerate(words, 1):
    print(f"'{word}'", end=" "* 2)
    if i % 5 == 0:
        print()

counts = Counter(words)

print("\nWord counts:")
for word, count in counts.items():
    print(f"{word}: {count}")
