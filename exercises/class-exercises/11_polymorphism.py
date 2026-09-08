# Exercise 11 — Polymorphism

# File: 11_polymorphism.py

# Create these two classes:

# CustomerAnalyzer
# Create an analyze() method.
# Return "Analyzing customer feedback".
# ProductAnalyzer
# Create an analyze() method.
# Return "Analyzing product data".

# Then:

# Create one object of each class.
# Call analyze() on both objects.
# Print the results.
# Expected Output
# Analyzing customer feedback
# Analyzing product data

# Goal: Understand how the same method name (analyze()) can perform different actions depending on the object.

class CustomerAnalyzer:
    def analyze(self):
        return "Analyzing customer feedback"

class ProductAnalyzer:
    def analyze(self):
        return "Analyzing product data"

ca_object = CustomerAnalyzer()
pa_object = ProductAnalyzer()

print(ca_object.analyze(),pa_object.analyze(),sep="\n")