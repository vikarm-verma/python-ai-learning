# Exercise 3 — Get Gemini Response

# File: exercise_03_get_response.py

# Use Case: Create a simple Python program that sends a fixed question to Gemini and displays the AI-generated response.

# Task:

# Use the Gemini client.
# Send the question: “What is Python?”
# Store Gemini's response in a variable called answer.
# Print answer.

# Goal: Understand how to receive and store an AI response in a Python variable.

# No: input(), loops, lists, or dictionaries.

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

question = "What is Python?"

prompt = f"""
Generate response in one line only
question:
{question}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = prompt
)

answer = response.text

print(answer)