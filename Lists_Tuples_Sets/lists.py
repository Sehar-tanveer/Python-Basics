#Lists
fruits = ["apple", "banana", "cherry"]
print("List of Fruits:", fruits)

# Length of list
print("Length of fruits:", len(fruits))

# Indexing & slicing
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice fruits[1:]:", fruits[1:]) 

# Add items
fruits.append("date")
print("After append:", fruits)

fruits.insert(0, "banana")
print("After insert:", fruits)

fruits_2 = ["pineapple", "mango"]
# fruits.insert(0, fruits_2)
# print("After insert:", fruits[0])

fruits.extend(fruits_2)
print("After extend:", fruits)

# Remove items
fruits.remove("apple")
print("After remove 'apple':", fruits)

fruits.pop()
print("After pop:", fruits)

fruits.sort()
print("After Sort:", fruits)
fruits.sort(reverse=True)
print("After Reverse Sort:", fruits)

print(max(fruits))
print(min(fruits))

# Modify (lists are mutable)
fruits[1] = "blueberry"
print("After change:", fruits)

# Looping through list
print("Loop through list:")
for f in fruits:
    print("Fruit:", f)

print()

for index, f in enumerate(fruits):
    print(index, f)

print()  

for index, f in enumerate(fruits, start=1):
    print(index, f)

print()    

# Join all fruits with a space
# sentence = " ".join(fruits)
# sentence = ", ".join(fruits)
sentence = " - ".join(fruits)
new_fruits = sentence.split(' - ')
print(sentence)    
print(new_fruits)