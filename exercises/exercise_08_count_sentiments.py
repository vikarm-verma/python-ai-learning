# Exercise 8 — Count Results

# File: exercise_08_count_sentiments.py

# Use Case

# You have a list of AI-generated customer feedback results. You need to count how many responses are Positive and how many are Negative.

# Given Data
# results = [
#     {"question": "Product quality?", "answer": "Positive"},
#     {"question": "Delivery experience?", "answer": "Negative"},
#     {"question": "Customer support?", "answer": "Positive"},
#     {"question": "Price?", "answer": "Positive"}
# ]
# Task
# Process the results list.
# Count the number of Positive answers.
# Count the number of Negative answers.
# Print both counts.
# Expected Output
# Positive: 3
# Negative: 1
# Goal

# Practice using lists, dictionaries, loops, if conditions, and counters to analyze AI-generated results.

# Hint: Create two counter variables and use an if condition inside a for loop.







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
    generate response in one line only, and provide your one word sentiment for answer as Positive
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
        
print(f"Positives: {c_positive} \n Negatives:{c_negative}")        

# for re in range(len(result)):
#     print(result)
#     print(re)
#     if result[re]["answer"] == "Positive":
#         c_positive=c_positive+1;
#     else:
#         c_negative+c_negative+1;
        
# print(f"Positives: {c_positive} \n Negatives:{c_negative}")
        