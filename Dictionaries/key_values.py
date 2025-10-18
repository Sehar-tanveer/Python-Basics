#Dictionary
student = {
    "name": "Ali",
    "age": 22,
    "address": ["Shahdra", "Lahore"]
}
print("Student Dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])

# Using get() method
print("Address:", student.get("address"))
print("Country:", student.get("country", "Not Found"))

# Add new key-value pair
student["country"] = "Pakistan"
print("After adding Country:", student.get("country", "Not Found"))

# Update a value
student["age"] = 23
print("After updating age:", student)

student.update({
    "name": "Anum",
    "age": 20,
    "address": ["Model Town", "Lahore"]
})
print("After update:", student)

# Delete
del student['age']
print("After Delete Age:", student)

# age = student.pop('age')
# print(student)
# print("Age:", age)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

# for loop
for key in student:
    print(key)

for key, value in student.items():
    print(key, ":", value) 