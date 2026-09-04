# Exercise 10 — Filter Positive Feedback

# File: exercise_10_filter_positive.py

# Use Case

# You have customer feedback analyzed by Gemini. Now you want to create a separate list containing only the Positive feedback.

# Given Data

# Use the result list generated in Exercise 9.

# Task
# Loop through the result list.
# Check whether the "answer" contains "Positive".
# If it is Positive, add that complete dictionary to a new list called positive_results.
# Print positive_results.
# Expected Output

# The output should contain only the dictionaries whose sentiment is Positive.

# Example:

# [
#     {
#         "question": "The product quality is excellent.",
#         "answer": "Positive"
#     },
#     {
#         "question": "Customer support was helpful.",
#         "answer": "Positive"
#     }
# ]
# Goal

# Practice creating a new list from existing data using a for loop and if condition.

# Hint: Start with an empty list:

# positive_results = []

# Then use .append() when the condition is true.





from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

questions = [
    "The product quality is excellent.",
    "The delivery was very late.",
    "Customer support was helpful.",
    "The product price is too high."
]

result=[]

for question in questions:
    
    prompt =f"""
    provide your one word sentiment for answer as Positive
    or Negative

    question:
    {question}
    """


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= prompt
    )

    result.append({
        "question":question,
        "answer":response.text.strip()
    })
positive_results=[];

for re in range(len(result)):
    if "Positive" in result[re]["answer"]:
        positive_results.append(result[re])
        
for re in positive_results:        
    print(f" Question :{re["question"]}\n Answer:{re["answer"]}")