# Exercise 5 — Encapsulation

# File: 05_encapsulation.py

# Task

# Create a CustomerAnalyzer class.

# Store customer feedback in a _feedback attribute.
# Create an update_feedback() method to change the feedback.
# Create an analyze() method that returns the current feedback.
# Create one customer object.
# Print the initial feedback.
# Update the feedback using update_feedback().
# Print the updated feedback using analyze().
# Expected Output
# Initial Feedback: The product is good.
# Updated Feedback: The product quality is excellent.

# Goal: Practice controlling object data through class methods.

class CustomerAnalyzer:
    _feedback ='The product is good'
    
    def update_feedback(self, feedback):
        self._feedback = feedback
    
    def analyze(self):
        return self._feedback
    
customer1 = CustomerAnalyzer()
print(customer1.analyze()) 

customer1.update_feedback("The Product Quality is excellent")
print(customer1.analyze())   
        
    