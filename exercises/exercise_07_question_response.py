# Exercise 7 — Store Question and Response Together

# File: exercise_07_question_response.py

# Use Case: Create a simple AI Q&A program that keeps track of both the questions sent to Gemini and the responses received.

# Task:

# Use the same three questions from Exercise 6.
# Use a for loop to process each question.
# Send each question to Gemini.
# Store the question and its response together.
# Store all the records in a list called results.
# Print results.

# Expected structure:

# [
#     {
#         "question": "What is Python?",
#         "answer": "Python is..."
#     },
#     {
#         "question": "What is Artificial Intelligence?",
#         "answer": "Artificial Intelligence is..."
#     }
# ]

# Goal: Understand how to use a dictionary inside a list to store structured AI results.

# Hint:

# result = {
#     "question": question,
#     "answer": answer
# }

# Then add result to your results list.


from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

questions=[
    "What is Python?",
    "What is Artificial Intelligence?",
    "What is Machine Learning?"
]

result=[]

for question in questions:
    
    prompt =f"""
    generate response in one line only

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
    
print(result)