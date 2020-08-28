import os
os.system('clear')

name = "Ben Mastersoft"

#Concantenation
greetings = "hello, my name is " + name
print(greetings)

#Change of Cases
print(greetings.upper())
print(greetings.lower())
print(greetings.capitalize())
print(greetings.title())
print(greetings.swapcase())

#length of a String
print(len(greetings))
print(greetings[13])
print(greetings[18:21])

#String Splitting
res = greetings.split(" ")
print(res)
print(res[4:6])