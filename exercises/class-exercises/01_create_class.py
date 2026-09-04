# Exercise 1 — Create Your First Class

# File: 01_create_class.py

# Task

# Create a class called Customer.

# Inside the class:

# Create a name attribute.
# Create an email attribute.

# Then create one object of the Customer class and assign a name and email to it.

# Finally, print the customer's details.

# Expected Output
# Customer Name: John
# Customer Email: john@example.com
# Goal

# Understand the basic relationship:

# Class → Object → Attributes

# No __init__() or methods yet.

class Customer:
    name='Vikram verma'
    email='vikram@gmail.com'
Customer1 = Customer();
print(f"Customer names is :{Customer1.name}\nCustomer email is: {Customer1.email}")
