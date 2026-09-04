# Exercise 18 — Handle Multiple Exceptions

# File: exercise_18_exception_handling.py

# Task

# Write a program that:

# Asks the user for a number.
# Converts it to an integer.
# Divides 100 by that number.
# Handles both possible errors:
# ValueError → user enters invalid input.
# ZeroDivisionError → user enters 0.
# Use else to print the result when there is no error.
# Use finally to print "Operation completed."
# Expected Output

# For input:

# 20
# Result: 5.0
# Operation completed.

# For input:

# 0
# Cannot divide by zero.
# Operation completed.

# For input:

# hello
# Invalid number.
# Operation completed.

try:
    number = int(input("enter a number :"))
    number = 100/number
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("zero cannot be divided")
else:
    print(f"number is {number}")
finally:
    print(f"task completed")