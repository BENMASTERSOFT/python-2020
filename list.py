import os
os.system('clear')

name = "Ben Mastersoft"
############################################
# Data Types
# Strings
# Numbers
# Lists
# Tuple
# Dictionaries
# Boolean
##########################################

names = ["John", "Bob", 'Tina']
print(names[0:3])

print("# Updating a List")
names[0] = "Jonathan"
print(names)

print("# Adding or Appending to List")
names=["Benjamin",41]
print(names)

print("#Appending item to list")
fruits = ["Apple", "Banana"]

# 1. append()
# print(f'Current Fruits List {fruits}')

# f = input("Please enter a fruit name:\n")
# fruits.append(f)

# print(f'Updated Fruits List {fruits}')

# print("# Inserting item to a list")
# num_list = [1, 2, 3, 4, 5]

# print(f'Current Numbers List {num_list}')

# num = int(input("Please enter a number to add to list:\n"))

# index = int(input(f'Please enter the index between 0 and {len(num_list) - 1} to add the number:\n'))

# num_list.insert(index, num)

# print(f'Updated Numbers List {num_list}')

# print("# Extending list")
# list_num = []
# list_num.extend([1, 2])  # extending list elements
# print(list_num)
# list_num.extend((3, 4))  # extending tuple elements
# print(list_num)
# list_num.extend("ABC")  # extending string elements
# print(list_num)
nums = [1,2,3,4,5]
names = [fruits,nums]
print(names)
print(names[1][1])