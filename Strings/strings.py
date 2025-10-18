print("Hello World")

# Single-quote within text
message = 'It\'s Universe'
print(message)

# Length of a String
print(len(message))

# To find index 
print(message[0])

# Single-quoted and double-quoted strings
s1 = 'Hello'
s2 = "World"
print(s1, s2)

# Triple-quoted strings
s3 = """This is a
multi-line string."""
print(s3)

# String Concatenation
hello_world = s1 + " " + s2
print("Concatenation 1:", hello_world)

s4 = '{}, {}. Welcome!'.format(s1, s2)
print("Concatenation 2:", s4)

s5 = f'{s1}, {s2.upper()}. Welcome!'
print("Concatenation 3:", s5)

# String Methods
text = "  Hello, Python!  "
print("lower():", text.lower())
print("upper():", text.upper())
print("count('Hello'):", text.count('Hello'))

# find
print("find():", text.find("Python"))

new_text = text.replace('Python', 'World')
print("replace():", new_text)

# String Formatting 
name = "Alice"
age = 30

# Using str.format()
msg1 = "Name: {}, Age: {}".format(name, age)
print(msg1)

# Using f-strings (Python 3.6+)
msg2 = f"Name: {name}, Age: {age}"
print(msg2)
