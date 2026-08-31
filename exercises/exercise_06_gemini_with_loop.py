# Exercise 6 — Use a Loop with Gemini

# File: exercise_06_gemini_with_loop.py

# Use Case: You have three questions that need to be answered by Gemini. Instead of writing the Gemini code three times, use a for loop to process all questions.

# Questions:

# What is Python?
# What is Artificial Intelligence?
# What is Machine Learning?

# Task:

# Create a list containing the three questions.
# Create an empty list called responses.
# Use a for loop to go through each question.
# Send each question to Gemini.
# Store each Gemini response in responses.
# Print the final responses list.

# Goal: Understand how a Python loop can automate repeated AI tasks.

# Hint:

# for question in questions:
#     # send question to Gemini
#     # store response

# No dictionaries yet.

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

responses=[]

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

    responses.append(response.text.strip())
    
print(responses)