
# Dictionary operations
dict1 = {
    '1': "Sunny",
    '2': "Reena"
}

print(dict1)

nameOf1 = dict1['1']
print(nameOf1)

for key, value in dict1.items():
    print(key, value)

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

fruits = {
    "apple": "red",
    "banana": "yellow",
    "grapes": "green",
    "berry": "pink"
}

print(fruits)

fruit1 = fruits['apple']
print(fruit1)

for key, value in fruits.items():
    print(key, value)

fruits.update({"watermelon": "dark green"})
print(fruits)

fruits.update({"grapes": "dark green"})
print(fruits)

# Set operations
set1 = {"1", "2", "3", "4"}
print(set1)

list1 = [1, 2, 3, 4, 1, 2, 1, 1]
set2 = set(list1)
set2.add(66)
set2.remove(1)
print(set2)

if 50 in set2:
    print("Yes, 50 is present")
else:
    print("Not present")

set_union = set1.union(set2)
print(set_union)

set_intersect = set1.intersection(set2)
print(set_intersect)
