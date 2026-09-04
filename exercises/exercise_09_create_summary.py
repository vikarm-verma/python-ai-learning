# Exercise 9 — Create a Summary

# File: exercise_09_create_summary.py

# Use Case

# You have collected multiple customer feedback responses from Gemini. Now you need to create a simple summary showing:

# Total number of responses
# Number of Positive responses
# Number of Negative responses
# Given Data

# Use the live Gemini approach that you used in Exercise 8. Your questions can be:

# questions = [
#     "The product quality is excellent.",
#     "The delivery was very late.",
#     "Customer support was helpful.",
#     "The product price is too high."
# ]
# Task
# Send each statement to Gemini.
# Ask Gemini to return the sentiment as Positive or Negative.
# Store each statement and Gemini's response in a list of dictionaries.
# Count Positive and Negative responses.
# Calculate the total number of responses.
# Print a summary.
# Expected Output

# The exact counts may vary depending on Gemini's response, but the format should be:

# Total Responses: 4
# Positive: 2
# Negative: 2
# Goal

# Practice combining everything you have learned so far:

# list → loop → dictionary → Gemini response → if condition → counters → output

# No new Python concept is required for this exercise.

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
c_positive =0
c_negative=0

for re in range(len(result)):
    print(f""" question: {result[re]["question"]} '\n' answer: {result[re]["answer"]}""" )
    if "Positive" in result[re]["answer"]:
        c_positive= c_positive+1
    elif "Negative" in result[re]["answer"]:
        c_negative=c_negative+1;
        
print(f"Total responses:{c_positive+c_negative} \n Positives: {c_positive} \n Negatives:{c_negative}")       