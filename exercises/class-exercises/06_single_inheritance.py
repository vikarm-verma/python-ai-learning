# Exercise 6 — Single Inheritance

# File: 06_single_inheritance.py

# Task

# Create a parent class called AIAnalyzer.

# Add a method analyze() that returns "AI analysis started".

# Create a child class called CustomerAnalyzer that inherits from AIAnalyzer.

# Create an object of CustomerAnalyzer.
# Call the inherited analyze() method.
# Print the returned result.
# Expected Output
# AI analysis started

# Goal: Practice Single Inheritance — one child class inheriting from one parent class.

class AIAnalyzer:
    def analyze(self):
        return "AI analysis started"
    
class CustomerAnalyzer(AIAnalyzer):
    pass
object1 = CustomerAnalyzer()
print(object1.analyze())
    