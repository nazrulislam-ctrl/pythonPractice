# print("Hello World")

# print(7+5)

# print(8*8)

# -----1. line gap-----

# print(" Hey, this is me \nMd. Nazrul Islam")

# -----2. Variable and Data type-----

# a= 1234512
# print(a)
# b= "Nazrul"
# print(b)
# c= True
# print("The type of a is", type(a))
# print("The type of b is",  type(b))
# print("The type of c is",  type(c))


# -----3. Arithmetic Operation-----

# ---Addition---
# a= 2+3
# print(a)

# ---Substraction---
# b= 6-5
# print(b)

# ---Multiplicatoin---
# c= 4*5
# print(c)

# ---Modulas---
# d= 5%3
# print(d)

# ---float division---
# e= 15/7
# print(e)

# ---Floor operation---
# print(15//7)

# -----4. TypeCasting in python-----

# a= "1"
# b= "3"
# print(a+b)
# print(int(a)+ int(b))

# Implicit TypeCasting


# -----5. Taking Input-----

# number= input("Please inter a number:")
# print(number)

# ---Input as a String---
# x=input("Enter First Number:")
# y=input("Enter Second Number:")
# print(x+y)

# ---Input as an Integer---
# x=int(input("Enter First Number:"))
# y=int(input("Enter Second Number:"))
# print(x+y)

# ---or---

# x=input("Enter First Number:")
# y=input("Enter Second Number:")
# print(int(x)+int(y))

# -----6.Multi line String-----
# DoubleQuote= 'Hello "This is" Md. Nazrul Islam'
# print(DoubleQuote)

# Multiline= '''Hello
# "This is"
# Md. Nazrul Islam'''
# print(Multiline)

# -----7. String Slicein-----
# name= "Nazrul"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[0],name[1],name[2],name[3],name[4],name[5])

# myName= "Md. Nazrul Islam"
# print(len(myName))
# print(myName[0:10])
# print(myName[4:10])
# print(myName[0:-6]) # It workd like:  print(myName[0:len(myName)-6])

#-----8. String Methods-----

# a="Nazrul !!!!"
# print(a.upper()) # Upper method used to make the whole string in upper case
# print(a.lower())  #Lower method used to make the whole string in lower case

# print(a.rstrip("!"))  #right strip
# print(a.replace("Nazrul", "Bulbul"))  #replace method used to replce the existing string to another one.

# b= " my name is Md. Nazrul Islam"
# print(b.split()) #split method
# c=b.lstrip(" ") #left strip removes space 
# print(c.capitalize())  #after removing space capitalize method capitalize the First letter "m"

# print(len(b))
# print((b.center(50)))
# print(len(b.center(50)))

# print(b.count("m"))
# print(b.endswith("Islam"))
# print(b.endswith("Md.", 5, 15))  #Ending word, starting index position, ending word index position
# print(b.find("is"))
# print(b.index("is"))