# Exercise 2 — Customer Class with __init__()

# File: 02_class_init.py

# Task

# Create a Customer class using __init__().

# The class should accept:

# name
# email

# Store both values as object attributes.

# Then:

# Create two customer objects with different names and emails.
# Print the details of both customers.
# Expected Output
# Customer Name: John
# Customer Email: john@example.com

# Customer Name: Sarah
# Customer Email: sarah@example.com

# Goal: Practice creating objects and automatically initializing their data using __init__().

class Customer:
    name=''
    email=''
    def __init__(self, name,email):
        self.name=name
        self.email=email
        
customer1 = Customer("Rahul","rahul@gmail.com")
customer2 = Customer("Ravi","ravi@gmail.com")        

print(f"customer1 details: {customer1.name}{customer1.email}\ncustomer2 details: {customer2.name}{customer2.email}")
        