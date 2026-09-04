# Exercise 10 — Hybrid Inheritance

# File: 10_hybrid_inheritance.py

# Create these classes:

# AIAnalyzer with analyze() method.
# CustomerAnalyzer inheriting from AIAnalyzer.
# ProductAnalyzer inheriting from AIAnalyzer.
# ReportAnalyzer inheriting from both CustomerAnalyzer and ProductAnalyzer.

# Create a ReportAnalyzer object and call the inherited analyze() method.

# Expected Output
# AI analysis started

# Goal: Practice combining inheritance structures in a single hierarchy.

class AIAnalyzer:
    def analyse(self):
        return "AI analysis started"

class CustomerAnalyzer(AIAnalyzer):
    pass

class ProductAnalyzer(AIAnalyzer):
    pass

class ReportAnalyzer(CustomerAnalyzer, ProductAnalyzer):
    pass

ra_object = ReportAnalyzer()
print(ra_object.analyse())