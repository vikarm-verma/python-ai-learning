# Exercise 5 — Store Multiple AI Responses

# File: exercise_05_store_responses.py

# Use Case: Create a program that asks Gemini three questions and stores all three responses in a Python list.

# Questions:

# What is Python?
# What is Artificial Intelligence?
# What is Machine Learning?

# Task:

# Send all three questions to Gemini.
# Store each response in a list called responses.
# Print the responses list.

# Goal: Understand how to store multiple AI responses in a Python list.

# No: loops yet. Handle the three questions manually.

# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# questions=[
#     "What is Python?",
#     "What is Artificial Intelligence?",
#     "What is Machine Learning?"
# ]

# prompt =f"""
# generate response in one line only

# questions:
# {questions}
# """


# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents= prompt
# )

# answer = [response.text.strip()]

# print(answer)

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

questions = [
    "What is Python?",
    "What is Artificial Intelligence?",
    "What is Machine Learning?"
]

responses = []

response1 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=questions[0]
)

responses.append(response1.text.strip())


response2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=questions[1]
)

responses.append(response2.text.strip())


response3 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=questions[2]
)

responses.append(response3.text.strip())


print(responses)