# Exercise 3 — Create an AI Analysis Method

# File: 03_class_method.py

# Task

# Create a class called CustomerAnalyzer.

# Use __init__() to store a feedback.
# Create a method called analyze().
# Inside analyze(), print the feedback.
# Create two objects with different feedback.
# Call analyze() for both objects.
# Expected Output
# Analyzing: The product quality is excellent.
# Analyzing: The delivery was very late.

# Goal: Understand Class → Object → Attribute → Method → self.

class CustomerAnalyzer:
    def __init__(self,feedback):
        self.feedback=feedback
    
    def analyze(self):
        print(f"feedback is {self.feedback}")
    
object1 = CustomerAnalyzer("Feedback is good")
object2 = CustomerAnalyzer("Feedback is poor")

object1.analyze()
object2.analyze()
    