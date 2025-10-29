# Q64. Demonstrate string functions

text = " Hello, World! "
print("Original text:", repr(text))

# Changing case
lowercase_text = text.lower()
uppercase_text = text.upper()
title_text = text.title()

print("\n\nLowercase:", lowercase_text)
print("Uppercase:", uppercase_text)
print("Title Case:", title_text)

# Trimming whitespace
stripped_text = text.strip()
left_stripped_text = text.lstrip()
right_stripped_text = text.rstrip()

print("\n\nStripped (both sides):", repr(stripped_text))
print("Left stripped:", repr(left_stripped_text))
print("Right stripped:", repr(right_stripped_text))

# Splitting and joining
words = stripped_text.split(",")
joined_text = "-".join(words)

print("\n\nSplit by comma:", words)
print("Joined with '-':", joined_text)

# Replacing and finding
replaced_text = stripped_text.replace("World", "Python")
index = stripped_text.find("World")
count = stripped_text.count("o")

print("\n\nReplaced text:", replaced_text)
print("Index of 'World':", index)
print("Count of 'o':", count)

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")
