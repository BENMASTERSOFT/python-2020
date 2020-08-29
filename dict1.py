import os
os.system('clear')


############################################
# Data Types
# Strings
# Numbers
# Lists
# Tuple
# Dictionaries
# Boolean
##########################################
mydad = {
  "child1" : {
    "name" : "Emil",
    "year" : 2002
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2003
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2005
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "mydad"  : mydad,
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print("################# My Dad Family ##########################")
print(myfamily['mydad'])
print()
print("################ The dict() Constructor #############")
print('thisdict = dict(brand="Ford", model="Mustang", year=1964)')
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print()

print("# note that keywords are not string literals")
print("# note the use of equals rather than colon for the assignment")
print()
print(thisdict)

print()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

print("# Create a dictionary with 3 keys, all with the value ")
print()
x = ('key1', 'key2', 'key3')
y = 5

thisdict = dict.fromkeys(x, y)

print(thisdict)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
print(car)