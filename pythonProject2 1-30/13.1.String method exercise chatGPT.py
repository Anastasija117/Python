# Given string
# "   Welcome to the world of Python programming! Learning Python is fun.  "
text = input("Write your text: ")

# 1. Convert the string to uppercase
uppercase_text = text.upper()
print("Uppercase:", uppercase_text)

# 2. Convert the string to lowercase
lowercase_text = text.lower()
print("Lowercase:", lowercase_text)

# 3. Count how many times the word "python" appears (case-insensitive)
python_count = text.lower().count("python")
print("Count of 'python':", python_count)

# 4. Find the position of the first occurrence of the word "learning"
learning_position = text.lower().find("learning")
print("Position of 'learning':", learning_position)

# 5. Replace the word "programming" with "coding"
replaced_text = text.replace("programming", "coding")
print("After replacing 'programming' with 'coding':", replaced_text)

# 6. Remove leading and trailing whitespaces
stripped_text = text.strip()
print("After stripping whitespaces:", stripped_text)

# 7. Check if the string starts with "Welcome"
starts_with_welcome = text.startswith("Welcome")
print("Does the string start with 'Welcome'?", starts_with_welcome)

# 8. Check if the string ends with "Python"
ends_with_python = text.endswith("Python")
print("Does the string end with 'Python'?", ends_with_python)

# 9. Split the string into a list of words
split_text = text.split()
print("List of words:", split_text)

# 10. Join the words back into a single string
rejoined_text = " ".join(split_text)
print("Rejoined string:", rejoined_text)

# Bonus Challenge: Check if the string contains only alphabetic characters, ignoring spaces
# Remove spaces and check if the remaining characters are alphabetic
is_alphabetic = text.replace(" ", "").isalpha()
print("Does the string contain only alphabetic characters (ignoring spaces)?", is_alphabetic)

input("end")