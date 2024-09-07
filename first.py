# print("my name is dilal hassan", "my age is 20")
# print("my age is 20")
# print("now im larnar full stack development")
# print(23)
# print(50+40)

# name = "dilal hassan"
# age = 20
# price = 99.99
# print(name)
# print("my name is :", name)
# print("my age is :", age)

# age = 20
# old = False
# a = None
# print(type(old))
# print(type(a))


# a = 2
# b = 5
# sum = a + b
# print(sum)

# a = 10
# b = 5
# div = a - b
# print(div)

# a = 5
# b = 5
# mul = a * b
# print(mul)

# a = 10
# b = 5
# dev = a / b
# print(dev)



# taking input from user & printing it

# name = input("name :")
# print(name)

# name = input("name :")
# age = int(input("age :"))
# price = float(input("price :"))

# print("my name is",name, "and i am",age, "years old")


# Conditional statements

# light = input("light color:")

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")        


# Grades is student

# marks = int(input("marks :"))
# if(marks >= 90):
#     print("A")
# elif(marks >= 80 and marks < 90):
#     print("B")
# elif(marks >= 70 and marks < 80):
#     print("C")
# else:
#     print("D")



#single line if Ternary Operator

# food = input("food :")
# eat = "Yes" if food == "cake" else "no"
# print(eat)


#Clever if Ternary Operator

# age = int(input("age :"))
# vote = ("yes", "no") [age <= 18]
# print(vote)

# sal = float(input("salary : "))
# tax = sal*(0.1, 0.2) [sal >= 50000]
# print(tax)


#type conversion

# a = 2
# b = 4.25
# sum = a + b
# print(sum)



# string function

# str = "i am starting python from appna college"
# print(str.endswith("ege"))

# str = "i am starting python from appna college"
# print(str.capitalize())

# str = "i am starting python from appna college"
# print(str.replace("o", "a"))

# str = "i am starting python from appna college"
# print(str.find("o"))

# str = "i am starting python from appna college"
# print(str.count("o"))




# Lists in python

# marks = [29.90, 30, 68.90, 90,98.89, 99]
# print(marks)


# Lists in methods
#append
# list = [1, 2, 3]
# list.append(4)
# print(list)

#sort ascending
# list = [1, 2, 3]
# print(list.sort())
# print(list)

#sort descending
# list = [1, 2, 3]
# print(list.sort(revers=True))
# print(list)

#revers
# list = ["a", "f", "c"]
# print(list.revers())
# print(list)

#insert
# list = [2, 1, 3]
# list.insert(1, 5)
# print(list)

#remove
# list = [2, 1, 3]
# list.remove(1)
# print(list)

#pop
# list = [2, 1, 3]
# list.pop(2)
# print(list)


#tuples in Python

# tup = (2, 1, 3, 1)
# print(tup)

# tup = (1)
# print(tup)
# print(type(tup))

# tup = (1.1)
# print(tup)
# print(type(tup))

#pratice question
# WAP to ask the user to enter name of their 3 favorate movies & stor tham in a list
# movies = []
# movi1 = input("enter list movi")
# movi2 =  input("enter list movi")
# movi3 = input("enter list movi")
# movies.append(movi1)
# movies.append(movi2)
# movies.append(movi3)
# print(movies)

# WAP to check if a list contains a palindrome of elements
# list1 = [1, 2, 1]
# list2 = [1, 2, 3]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")



# dictionary in python

# info = {
#     "name" : "dilal hassan",
#     "cgpa" : "8.6",
#     "marks" : "97, 89, 90"
# }
# print(info)


# nested dictonary

# student = {
#     "name" : "dilal hassan",
#     "subject" : {
#         "phy" : 92,
#         "math" : 85,
#         "scince" : 90,
#         "javascript" : 96,
#     }
# }
# print(student)


# dictonary methods  keya(), values(), items(), get("key"), update(new),

# student = {
#     "name" : "dilal hassan",
#     "subject" : {
#         "phy" : 92,
#             "math" : 85,
#                 "scince" : 90,
#         "javascript" : 96,
#     }
# }
# print(student.keys())

# student = {
#     "name" : "dilal hassan",
#     "subject" : {
#         "phy" : 92,
#             "math" : 85,
#                 "scince" : 90,
#         "javascript" : 96,
#     }
# }
# print(student.values())


#set in python

# collection = {1, 2, 3, 4}
# print(collection)
# print(type(collection))




#loops in python
#while

# count = 1
# while count <= 6:
#     print("hello world")
#     count += 1

# i = 1
# while i <= 5:
#     print("dilal hassan", i)
#     i += 1

# i = 1
# while i <= 10:
#     print(3 * i)
#     i += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1



#for loops

nums = [1, 2, 3, 4, 5]
for dilal in nums:
    print(dilal)

#range loops

for i in range(1, 100):
    print(i)

for i in range(100, 0, -1):
    print(i)



#function in python     defination

# def cal_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# cal_sum(5, 10)
# cal_sum(10, 20)
# cal_sum(30, 40)
# cal_sum(10, 50)



# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()


#Built in functions

# print("dilal hassan", end="")
# print("munna")


#User defined functions

#default Parameters
# def cal_prod(a=2, b=3):
#     print(a * b)
#     return a * b
# cal_prod()

# cities = ["assam", "delhi", "noida", "pune", "chennai", "mumbi"]
# heroes = ["dilal", "iroman", "caption"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(heroes)

# cities = ["assam", "delhi", "noida", "pune", "chennai", "mumbi"]
# heroes = ["dilal", "iroman", "caption"]
# def print_len(list):
#     print(len(list))
# def print_len(list):
#     for item in list:
#         print(item, end=" ")
# print_len(heroes)
# print()


# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD", inr_val, "INR")
# converter(3)


#Recursion

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(4))




#File I/O in python
#types of file
#1 text File: .txt .docx .log ect.
#2 Binary File: mp4, mov, png, jpeg ect.

# with open("demo.text", "r") as f:
#     dataa = f.read()
#     print(dataa)

# with open("demo.text", "w") as f:
#     f.write("new data")



#oop in pytho

#class & object in python

#class
# class Student:
#     name = "dilal hassan"

# s1 = Student()
# print(s1.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"
# car1 = Car()
# print(car1.color)
# print(car1.brand)


# class Student:
#     name = "dilal hassan"
#        #default construtors
#     def __init__(self):
#         print("addin new student")

# s1 = Student()
# print(s1.name)

# class Student:
#     #parametries construtors
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("addin new student")

# s1 = Student("dilal", 99)
# print(s1.name, s1.marks)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("dilal hassan", [99, 98, 97])
# s1.get_avg()


# class Account:
#     def __init__(self, bal, acc):
#         self.blance = bal
#         self.account_no = acc

#     def debit(self, account):
#         self.blance -= account
#         print("Rs", account, "was debited()")
#         print("total blance =", self.get_blance())

#     def credit(self, account):
#         self.blance -= account
#         print("Rs", account, "was credited()")
#         print("total blance =", self.get_blance())

#     def get_blance(self):
#         return self.blance
    
# acc1 = Account(100000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(400000)


#oops 2

#del keyword


# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stop")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# Car1 = ToyotaCar("fortuner")
# Car2 = ToyotaCar("price")

# print(Car1.start)



#supper method

#class method
# class Person:
#     name = "munna"

# def changeName(self, name):
#     self.name = name

# p1 = Person()
# p1.changeName("sandip")
# print(p1.name)
# print(Person.name)


#property

#polymorphism : Operater Overloding

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img, "j")

# num1 = Complex(1, 3)
# num1.showNumber()

# num1 = Complex(6, 4)
# num1.showNumber()




#mini project

# import random

# target = random.randint(1, 100)
# while True:
#     userChoice = input("Guss the target or Quit:")
#     if(userChoice == "Quit"):
#         break
#         print("Success : Correct Guess")
#         break
#     elif(userChoice < target):
#         print("your number to small. Take a bigger guess...")
#     else:
#         print("your number is to big. Take a small guess...")

# print("-----GAME OVER----")




#random password Generator

