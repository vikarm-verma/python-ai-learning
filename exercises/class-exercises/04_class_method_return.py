# Exercise 4 — Return an Analysis Result

# File: 04_class_method_return.py

# Task

# Create a CustomerAnalyzer class.

# Use __init__() to store feedback.
# Create an analyze() method.
# analyze() should return the feedback instead of printing it.
# Create two objects.
# Call analyze() for both objects.
# Store the returned values in variables.
# Print those variables.

# Goal: Understand return vs print() and how a method can send data back to the program.

class CustomerAnalyzer:
    def __init__(self,feedback):
        self.feedback=feedback
    
    def analyze(self):
        return self.feedback;
    
object1 = CustomerAnalyzer("Feedback is good")
object2 = CustomerAnalyzer("Feedback is poor")

print(object1.analyze())
print(object2.analyze())