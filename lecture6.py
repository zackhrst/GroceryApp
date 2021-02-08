# ## Cracking the coding interview. - book for addiitonal help with alogrithms, interviews, and such.
# ## Need to learn about GitHub... check notes last week

# ## CLASSES and OBJECTS  
# ## Learn how to build larger and scalable applications. 

# # Class is a blue print to represent something.

# Car:
#     - make
#     - model
#     - vin
#     - color


# Object is a concrete implementation of a Class
# Object represents a PARTICULAR CAR
# car = Car()
# car.make = "Tesla"
# car.model = "Model X"
# car.vin = "e2222323334eeee"
# car.color = "blue"

# # https://www.hackerrank.com/dashboard
# # https://edabit.com/
# # This is a great tutorial/challenge site: https://automatetheboringstuff.com/
# # https://leetcode.com/
# # https://www.practicepython.org/


# # Create a class to define a Person:

# #Person
#     - height = 65 inches
#     - weight = 170 pounds
#     - gender = male
#     - ethnicity = caucasian
#     - education = bachelor degree
#     - firstname
#     - lastname
#     - age
#     - 

# created a car class and defining the properties of the class.
# class Car: 
#     def __init__ (self):
#         self.make = "Honda"
#         self.model = "Accord"
#         self.vin = "34e3324V85"
#         self.color = "blue"

# # creat an instance/object of the Car class
# car = Car("Toyota", "Corolla")

# BankAccount
#  - account number
#  - routing number
#  - account owner 
#  - account type (checking, savings)
#  - balance
#  - name

# required properties to create an account: 
#     - account owner  (firstname, lastname, middlename)
#     - account type (checking, savings) 
#     - balance (default value of 0)


# Create a class called Table to represent a table
# In order to create an instance of the table, you must pass in width and geight of the table

class Table: 
    def __init__(self, width, height): #initializer/constuctor
        self.width = width
        self.height = height
        self.material = ""
        self.style = ""
        self.manufacturer = ""

# create a table object
table = Table(200,100)
print(table.width)
print(table.height)
