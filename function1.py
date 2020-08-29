import os
os.system('clear')


############################################
# function
# 
##########################################

def nameit(name):
  print("Hello " + name)

nameit("Ben")

print()

favourite_pizza = {
	"John":"Sugar",
	"Bob":"Pork", 
	'Tina':"Bread"
	# "dict2":("Mon":"Tea", "Tue":"Rice")
}

def dictdis(dis):
	for x,y in dis.items():
		print(x,y)

dictdis(favourite_pizza)
