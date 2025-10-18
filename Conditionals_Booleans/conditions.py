#Conditions
language = "Python"

# if else
if language == "Python":
    print("The language is Python")
elif language == "Java":
    print("The language is Java")
else: 
    print("No match")

#Boolean
user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin page")
else:
    print("Bad credentials")    

if not logged_in:
    print('Please login')    
else:
    print("Welcome")     

# Object Identity
a = [1, 2, 3]    
b = [1, 2, 3] 
b = a

print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))

# False Evaluations
condition = 10
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
