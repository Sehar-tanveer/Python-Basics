# Tuples

#Mutable
colors = ["red", "green", "blue"]
print(colors)

colors_2 = colors
print(colors_2)

colors[0] = "purple"
print(colors)
print(colors_2)

#Immutable
tuple_1 = ["red", "green", "blue"]
print(tuple_1)

tuple_2 = tuple_1
print(tuple_2)

tuple_1[0] = "purple"
print(tuple_1)
print(tuple_2)