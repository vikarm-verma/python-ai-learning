# Exercise 12 — Using super()

# File: 12_super_method.py

# Task

# Create a parent class called AIAnalyzer.

# Add __init__(self, model).
# Store the model in self.model.
# Add a method analyze() that returns "AI analysis started".

# Create a child class called CustomerAnalyzer that inherits from AIAnalyzer.

# Add __init__(self, model, customer).
# Use super() to call the parent class's __init__().
# Store the customer name in self.customer.
# Create a method customer_analysis() that returns both the customer name and model.

# Create an object and print the result.

# Expected Output
# Customer: John
# Model: Gemini

# Goal: Practice using super() to reuse the parent class's initialization while adding new attributes in the child class.

class AIAnalyzer:
    def __init__(self,model):
        self.model = model
    
    def analyze(self):
        return "AI analysis started"

class CustomerAnalyzer(AIAnalyzer):
    def __init__(self, model,customer):
        super().__init__(model)
        self.customer = customer
    
    def customer_analysis(self):
        return self.model, self.customer

ca_object = CustomerAnalyzer("New Model","Old Customer")
    
print(ca_object.customer_analysis())