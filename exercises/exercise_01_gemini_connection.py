# Exercise 1 — Gemini Connection

# File: exercise_01_gemini_connection.py

# Use Case: Connect a Python program to Gemini using an API key.

# Task:

# Import the required libraries.
# Load the .env file.
# Read the Gemini API key.
# Create the Gemini client using the API key.

# Goal: The program should run successfully without errors.

# No: User input, prompts, Gemini response, loops, or lists.


from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key= api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Where is Jaipur ?"
)

print(response.text)