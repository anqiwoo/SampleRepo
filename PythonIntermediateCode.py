# Python Intermediate
# * Tuple
a = (i for i in range(10))
print(type(a))
print(a)

b = (1, 2, 3, 4)
print(b[::-1])

# Unpacking in Tuple
my_tuple = "max", 27, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

# Unpacking Multiple variable with a star
my_tuple = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)

# Compare List and Tuple (Working with Tuple could be more efficient, since they are immutable)
import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))

# * Dictionary
mydict = {"name": "Vicky", "age": 21}
mydict2 = dict(name="Mary", age=26)  # Do not use quotes for the key in dict method
print(mydict)
print(mydict2["age"])

del mydict2["name"]
print(mydict2)

mydict.pop("name")
print(mydict)

mydict.popitem()
print(mydict)

# Merge two dicts
my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict2 = dict(name="Mary", age=27, city="Boston")
print(my_dict)
print(my_dict2)
my_dict.update(my_dict2)
print(my_dict)
print(my_dict2)

# Key Data Type of Dict
my_dict = {3: 9}
print(my_dict)

my_tuple = (8, 7)
mydict = {my_tuple: 6}  # Tuple could be the key of a dict, but not a list
print(mydict)

# * Set

