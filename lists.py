# *****In list we can make change and add values where as in tuples we cannot make changes*****
# marks= [20, 30, 40, 50, 85]
# print(marks)
# print(type(marks))
# print(marks[1])
# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[4-3])

# if "85" in marks:
#     print("Maybe!")
# elif 85 in marks:
#     print("Yes")
# else:
#     print("No")
    
# *****List Comprehension*****
# lst=[i for i in range(1,5)]
# print(lst)

# ****List Method*****

# l=[1,2,3,4,5,10, 7, 35, 25, 20]
# print(l)
# l.reverse() #make the list in reverse order
# print(l)
# l.append(6)
# print(l)
# l.sort()
# print(l)
# l.sort(reverse=True) # will be sort in descending order
# print(l)

# print(l.index(3))

# print(l.count(1))

# *** reference of the list***
# l=[1,2,3,4,5,10, 7, 35, 25, 20]
# m=l #it made the main list as a reference
# m[0]= 0
# print(l)
# print(m)

# ***To make a copy of the list***
# l=[1,2,3,4,5,10, 7, 35, 25, 20]
# c=l.copy()
# c[0]= 0
# print(l)
# print(c)
# l.insert(2, 425)
# print(l)

# ***extend() Method***
# l=[1,2,3,4,5,10, 7, 35, 25, 20]
# m=[100, 3000, 5000]
# l.extend(m)
# print(l)
# k=l+m
# print(k)

