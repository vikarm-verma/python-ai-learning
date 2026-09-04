# Exercise 7 — Multiple Inheritance

# File: 07_multiple_inheritance.py

# Task

# Create three classes:

# AIAnalyzer with an analyze() method.
# FeedbackProcessor with a process() method.
# CustomerAnalyzer that inherits from both classes.

# Create one CustomerAnalyzer object and call both inherited methods.

# Expected Output
# AI analysis started
# Feedback processed

# Goal: Practice Multiple Inheritance.

class AIAnalyzer:
    def analyze(self):
        return "AI analysis started"
    
class FeedbackProcessor:
    def process(self):
        return "Feedback Processed"
    
class CustomerAnalyzer(AIAnalyzer,FeedbackProcessor):
    pass

object1 = CustomerAnalyzer()
print(object1.analyze())
print(object1.process())