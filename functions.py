# # *****1. Function*****
# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)
# def isGreater(a,b):
#     if(a>b):
#         print("first number is greater")
#     else:
#         print("Second number is greater")

# # ***pass Method***
# def isLesser(a,b):
#     pass
# a=9
# b=3
# calculateGmean(a,b)
# isGreater(a,b)
# c=4
# d=6
# calculateGmean(c,d)
# isGreater(c,d)

# *****2. Default Arguments*****

# def average(a=9,b=1):
#     print("The average is", (a+b)/2)   
# average()

# ***For a lots of arguments as a tuple***
# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     return("Average is: ", sum/len(numbers))
    
# avg=average(4,5,6,2,3)
# print(avg)
# ***For a lots of arguments as a Dictionary***