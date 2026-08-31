# Exercise 2 — Send a Question to Gemini

# File: exercise_02_send_question.py

# Use Case: Send a fixed question from Python to Gemini.

# Task:

# Use the Gemini client you created in Exercise 1.
# Send this question to Gemini:

# What is Artificial Intelligence?

# Receive Gemini's response.
# Print the response.

# Goal: Python should successfully send a question to Gemini and display its answer.

# No: input(), loops, lists, or dictionaries.

from google import genai
from dotenv import load_dotenv
import os

#load all varibles of env in Python enviornment
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=" What is Artificial Intelligence?"
)

print(response.text)    