import math
import random




# Here im printing stuff

print("-----------------------")
# print("something") # This is me printing


#variable stores information
#integer (int) variable holds a whole number

age = 5
# print(age*10)
# print(type(age))

# something is the variable, 25 is the information

#floating point variable holds a decimal

decimalStuff = 12.0
# print(decimalStuff)
# print(type(decimalStuff))

#String variable holds a word

words = "apples"
# print(words)
# #
# print(type(words))
# print(words*age)

# booleans = True
# print(booleans)
# print(type(booleans))

# # Break sequences in strings
moreWords = "This is a test to see what happens"
# print(moreWords)
# moreWords = "This is a \"test to see what\" happens"
# print(moreWords)
# moreWords = "This is a \'test to see what\' happens\'"
# print(moreWords)
# moreWords = "This is a \\test to see what\\ happens"
# print(moreWords)
# moreWords = "This is a \ntest to see \nwhat happens"
# print(moreWords)
#
# #formated strings
age = 45
first = "Tom"
last = "Smith"
full = str(age)+" "+last
# print(full)
# # # #
things = f"{first} {last} is {age} years old"
# print(things)
# # #
full = f"{age/4} \n {5+6+56} {first}"
# print(full)


#Boolean Variables hold conditions True or False (Must be capitalized)

condition = False
otherCondition = False
#
# if (condition):
#     print("This is true")
#     if (condition):
#         print("It is also false")
#         print("It is also false2")
# elif(otherCondition):
#     print("Not true")
# else:
#     print("Something else")


#Programs get executed from top to bottom. If you use the same variable it gets overridden

age = 56
age1 = 67
# print(age)
decimalStuff = 12.3
# You can do math

age2 = age+decimalStuff
age3 = age/decimalStuff
age4 = age-decimalStuff
age5 = age2*decimalStuff
# print(age2)
# print(age3)
# print(age4)
# print(age5)
#
# Extra math
# // gives you the whole number. Gets rid of the numbers left of the decimal
age6 = age//decimalStuff
# print(age6)
#
# # % is known as the mod. It returns the remainder of the division
# age7 = age%decimalStuff
# print(age7)
#
# # ** two multiplications is the exponent. It is age to the power of decimalStuff
age8 = 67**2
# print(age8)

# Augmented operators
newAge = 20
# #
# newAge = newAge + 5
# print(newAge)
# #
newAge += 5
# print(newAge)
# #
# newAge = newAge - 10
# print(newAge)
# #
newAge -= 5
# print(newAge)
# #
newAge *= 2
# print(newAge)
# #
newAge %= 3
# print(newAge)

# Order of operations = Same as in math (mod counts as a type of divison)
x = 10+3*5
# print(x)
# #
x = (10+3)**5
# print(x)


# Careful with Strings and numbers

# stris = "apple"
# numb = 10
#
# addStuff = stris+" "+str(numb)
# print(addStuff)
#
# full = f"{stris} {34<12}"
# print(full)


# Getting input (by default it is String)

# number1 = float(input("What do you want your first number to be?: "))
# number2 = float(input("What do you want your second number to be?: "))
# input3 = input("What do you want to do? (add, sub, mult, div)")
# if(input3 == "add"):
#     print(f"This is the addition result: {number1+number2}")
# if(number1+number2 >= 200):
#             print("This is a big number")
# if(input3 == "mult"):
#     print(f"This is the multiplication result: {number1*number2}")
# if(input3 == "sub"):
#     print(f"This is the subtraction result: {number1-number2}")
# if(input3 == "div"):
#     print(f"This is the division result: {number1/number2}")




# intTest = int(igujerhb)
# print(intTest)


# if you want an integer so you can do math you have to recast it
# to print it you have to recast it as a string

# intIWant = int(input("This is the int I want: "))
# intIWant += 10
# print("This is the int you wanted "+str(intIWant))

# int doesn't have a decimal place. They are a whole numbers. 
# If you want to be able to have a decimal place you have to use float

# floatIWant = float(input("This is the float I want: "))
# print("This is the float you wanted "+str(floatIWant))

# You can also recast into a boolean
# But be careful. When using it directly on the input it just checks if they put something in.

# boolIwant = input("Is the statement True or False?: ")
#
# print(boolIwant)
#
# if (boolIwant is True):
#     print("The statement is True")
# else:
#     print("The statement is False")

# Some built in functions

name = "matt smith"
firstName = "matt"
lastName = "smith"
# age = 45
# #
# print(name.capitalize())
# print(f"{firstName.capitalize()} {lastName.capitalize()}")
# print(name.upper())
# print(name.lower())
# print(name.isprintable())
# print(name.__len__())
# print(len(name))
#
# # Think of a String as a list of characters. The list starts with 0


name = "matt Smith"
name = name.lower()
# print(name.find("smith"))
# print(name.__contains__("th"))
# # #
# name = name.replace("matt", "john")
# print(name.replace("t", "johnson"))
# print(name)

# name = name.replace("t", "johnson")
# # Careful when just usign print because you haven't saved it
# print(name)
#
# #Using the in operator
#
name2 = "matt"
# print(name2 in name)
# print(name.__contains__(name2))
# print("bob" in name)
# #
# name = name.replace("smith", "johnson")
#
# if("smith" in name):
#     print("Name is common")
# else:
#     print("Name is not common")


# Comparison operators

isit = 3 > 2
# print(isit)
# # # #
isit = 3 < 2
# print(isit)
# # # #
isit = 3 >= 2
# print(isit)
# # # #
isit = 3 <= 2
# print(isit)
# #
isit = 3 == 2
# print(isit)
# # # #
# # # ! means NOT
isit = 3 != 2
# print(isit)
# # # #
# # # # # not means NOT when you want the opposite of something
tom = not isit
# print(tom)
# print(not tom)

# Logical operators ->  and  or

age = 45
# print(age>35)
#
#
# print(age>60 and age<20)
#
#
# print(age>50 or age <49)
#
# print( age<50 or (age>60 and (age<35 or age>35)))


# if elif else
#
tom = 10

# if (tom<35):
#     print("He is young")
# elif (tom<12):
#     print("He is very young")
# elif (tom>11):
#     print("He is very young 2")
# elif (tom>9):
#     print("He is very young 3")
# else:
#     print("He is old")
#     print("this is the end")

#in one line if not complex
tom = 45
if (tom<35):
    message = "He is young"
else:
    message = "He is old"
# print(message)
#
message = "He is young" if tom<35 else "He is old 1"
# print(message)



# while loops

price = 20
# while (price>10):
#     print(str(price) + " is Too much")
#     price -= 1 
#     # must make sure to have something 
#     # in the loop to terminate the sequence by making the condition false. 
#     # If not it will go on forever.
# print(str(price) + " is Just right")


#
# sinStuff = math.sin(35)
# print(sinStuff)
# cosStuff = math.cos(45)
# print(cosStuff)

# Lists

names = ["Bob", "Tom", "John", "Matt", "James"]

# print(names)
#
# print(names.__len__())
# print(names.__contains__("Bob"))
# print(names[1])
# print(names[-3]) # remember index starts at 0
# print(names[names.__len__()- 1]) # remember index starts at 0
# names[2] = "Ash" # replace 
# print(names)
# print(names[3:names.__len__()]) # just want a few

# something = "Tom SmiTh"
# something = something.lower()
# print(something[1:4])
# print(something.replace("o", "i"))
# print(something.__contains__("smit"))

#
numbers = [1,2,5,8,34,25,16,1,2,3,2,4,2]
# print(numbers)
# print(numbers.__len__())
# print(numbers[12]) # don't go over
# print(numbers[-1]) # the last one
# print(numbers[-4]) # second to last one
#
# # List operations
numbers.append(3)
# print(numbers)
numbers.insert(4, 90)
# print(numbers)
numbers.remove(3)
# print(numbers)
# # numbers.remove(2)
while (2 in numbers):
    numbers.remove(2)
# print(numbers)
#
# print(numbers.__contains__(3))
# print(len(numbers)) # how many elements
# print(numbers.__len__())
# print(numbers.count(78)) # how many 2 are in the list
# print(numbers.index(34)) # where is 34?
# numbers.clear()
# print(numbers)

#check for info in list
numbers = [1,2,5,8,34,25,16]
names = ["Bob", "Tom", "John", "Matt", "James"]
#
# print("Tom" in numbers)
# print(2 in numbers)
# print(2 in names)
# print("Tom" in names)
# print("Tom " in names) # Careful

# for loops

numbers = [1,2,5,8,34,25,16]
names = ["Bob", "Tom", "John", "Matt", "James"]

# for bottle in numbers:
#     print(bottle+bottle)
# #
# print(bottle+bottle)
# for apples in names:
#     print("This is the name: "+apples)

# # same thing with while loops
# index = 0
# while (index<len(numbers)):
#     print(numbers[index])
#     index+=2
#
# # # while loops give you more flexibility
# index = len(numbers)-1
# while(index>=0):
#     print(numbers[index])
#     index-=2



# Using range funciton
numbers2 = range(0,101)
# print(numbers2)
# # # #
# for bubbles in numbers2:
#     print(bubbles)

# print(bubbles)

# numbers3 = range(-50,10100)
# for things in numbers3:
#     print(things)

# break - get out of loop

numbers3 = range(0,20)
# for stuff in numbers3:
#     if (stuff == 4):
#         print("Found it")
#         break
#     print("Not yet")
# print("done")

# functions
def goingUp (number=5, upBy=5):
     return number+upBy

# info = goingUp()
# print(info)
#
# #Using it from somewhere else
import moreTesting as mt
# #
info2 = mt.moreStuff(30, 15)
# print(info2)
# # # #
info3 = mt.moreStuff(50)
# print(info3)
# #
# info4 = moreTesting.moreStuff()
# print(info4)
# # # #
apples = [10, 4, 5, 7]
# print(moreTesting.moreStuff(apples))
#
# for something in apples:
#     print(moreTesting.moreStuff(something))

groups = ["Group 1","Group 2","Group 3","Group 4","Group 5","Group 6","Group 7"]
groupsRand=[]
index = 0
while (index<groups.__len__()):
    randChoice = random.choice(groups)
    if (not groupsRand.__contains__(randChoice)):
        groupsRand.append(randChoice)
        index+=1

print(groupsRand)
# print("Change testing 6")

print("-----------------------")