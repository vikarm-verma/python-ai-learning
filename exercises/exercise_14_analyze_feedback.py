# Exercise 14 — Analyze Filtered Feedback with Gemini

# File: exercise_14_analyze_feedback.py

# Use Case

# You already have the customer feedback file and can filter the entries that contain "support". Now use Gemini to analyze those filtered feedback entries.

# Task
# Read customer_feedback_filtered.txt line by line.
# Find only the feedback containing "support".
# Send each matching feedback to Gemini.
# Ask Gemini to return:
# The sentiment: Positive or Negative
# A one-line reason
# Store Gemini's response in a Python list.
# Print each feedback along with Gemini's response.
# Example Expected Output
# Feedback: Feedback 3: Customer support was helpful.
# Sentiment: Positive
# Reason: The customer had a good support experience.

# Feedback: Feedback 23: Customer support was helpful.
# Sentiment: Positive
# Reason: The customer found the support helpful.


from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

with open("../python-basics-of-ai/customer_feedback_filtered.txt","r")as r_file:
    feedback=[]
    support_feedback=[]
    matching_feedback=0
    for line in r_file:
        if "support" in line:
            support_feedback.append(line)
            # print(line)
            # matching_feedback+=1

prompt=f"""
       You need to perform following tasks: 
       
       1. Read a list which is carrying feedback containing "support" word in each feedback.
       
       2. Read each feedback and provide your sentiment on it either "Positive" or "Negative"
       
       3. Provide a one line reason regarding why are you putting that sentiment.
       
    Return in the below given format:
    
       Feedback : <feedback>
       Sentiment : <Positive or Negative>
       Reason : <One line reason>
       
    Do not add numbering or any extra text.
       
       list:
       {support_feedback}
       

       
       """

response= client.models.generate_content(
    model="gemini-2.5-flash",contents= prompt
)

gemini_response_list =[]
gemini_response_list.append(response)

for re in gemini_response_list:
    print(re)