# Exercise 17 — Handle Invalid Number Input

# File: exercise_17_value_error.py

# Task

# Write a program that:

# Takes a number from the user using input().
# Converts the input into an integer using int().
# Prints the number if the conversion is successful.
# Handles ValueError if the user enters something that is not a valid number.
# Expected Output

# For input:

# 25
# Number: 25

# For input:

# hello
# Invalid number.
# Constraint
# Use try
# Use except ValueError
# Do not use else or finally yet.

# Goal: Practice handling ValueError with user input.

try:
    number = int(input("enter a number"))
    print(number)
except ValueError:
    print("Invalid entry")