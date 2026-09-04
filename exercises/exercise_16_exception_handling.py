# Exercise 16 — Handle a Missing File

# File: exercise_16_exception_handling.py

# Task

# Write a program that tries to open customer_feedback_10000.txt in read mode.

# Use try and except FileNotFoundError to handle the error.

# If the file exists → print File opened successfully.
# If the file does not exist → print File not found.
# Constraint
# Use try
# Use except FileNotFoundError
# Do not use else or finally

# Goal: Practice basic exception handling with file operations.

try:
    with open("../python-basics-of-ai/customer_feedback_10000.txt","r")as r_file:
        data = r_file.read()
        print(data)

except FileNotFoundError:
    print("File not found")
    
    