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

favourite_pizza = {
	"John":"Sugar",
	"Bob":"Pork", 
	'Tina':"Bread"
	# "dict2":("Mon":"Tea", "Tue":"Rice")
}
print(favourite_pizza)
################################################
## calling specific item in dictionary
#
# print(favourite_pizza["Bob"]) #main code
#
###############################################

#########################################
## Deleting item from the Dictionary
#
# del favourite_pizza['Bob']  #main code
# print(favourite_pizza)  #main code
#
#########################################

# #Adding item to dictionary
#favourite_pizza.update({"Rose":"Milk","Emma":"Meat"}) #main code
#print(favourite_pizza)  #main code

## Updating existing item
favourite_pizza["Bob"] = "Orange"
print(favourite_pizza)


######################################
# Nested Dictionay
#
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
# print(myfamily)
os.system('clear')

print(myfamily["child1"])

