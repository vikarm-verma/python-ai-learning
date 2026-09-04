# Exercise 8 — Multilevel Inheritance

# File: 08_multilevel_inheritance.py

# Task

# Create these three classes:

# AIAnalyzer → method analyze()
# CustomerAnalyzer → inherits from AIAnalyzer and has method customer_info()
# PremiumCustomerAnalyzer → inherits from CustomerAnalyzer and has method premium_analysis()

# Create a PremiumCustomerAnalyzer object and call all three methods.

# Expected Output
# AI analysis started
# Customer information processed
# Premium customer analysis completed

# Goal: Practice Multilevel Inheritance:

# AIAnalyzer
#     ↓
# CustomerAnalyzer
#     ↓
# PremiumCustomerAnalyzer

class AiAnalyzer:
    def analyze(self):
        return "AI analysis started"

class CusotmerAnalyzer(AiAnalyzer):
    def customer_info(self):
        return "Customer information processed"

class PremiumCustomerAnalyzer(CusotmerAnalyzer):
    def premium_analysis(self):
        return "Premium customer analysis completed"
    
premium_object = PremiumCustomerAnalyzer()
print(premium_object.analyze(),
       premium_object.customer_info(),
       premium_object.premium_analysis(),sep="\n")