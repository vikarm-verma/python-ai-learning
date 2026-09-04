# Exercise 9 — Hierarchical Inheritance

# File: 09_hierarchical_inheritance.py

# Task

# Create:

# AIAnalyzer with an analyze() method.
# CustomerAnalyzer that inherits from AIAnalyzer.
# ProductAnalyzer that also inherits from AIAnalyzer.

# Create one object of each child class and call the inherited analyze() method.

# Expected Output
# AI analysis started
# AI analysis started

# Goal: Understand:

# AIAnalyzer
#    ↓
#    ├── CustomerAnalyzer
#    └── ProductAnalyzer




class AiAnalyzer:
    def analyze(self):
        return "AI analysis started"

class CusotmerAnalyzer(AiAnalyzer):
   pass

class ProductAnalyzer(AiAnalyzer):
    pass

ca_object = CusotmerAnalyzer()
pa_object = ProductAnalyzer()

print(ca_object.analyze(),pa_object.analyze(),sep="\n")
    