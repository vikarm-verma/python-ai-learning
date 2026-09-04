# Exercise 15 — Save AI Analysis to a File

# File: exercise_15_save_ai_results.py

# Use Case

# You have already filtered the customer feedback and sent the matching feedback to Gemini. Now, save Gemini's complete analysis into a new text file so it can be used later.

# Task
# Use the support_feedback list from Exercise 14.
# Send the list to Gemini.
# Receive the Gemini response.
# Save response.text into:
# support_feedback_analysis.txt
# Print a success message after saving the file.
# Expected Output
# AI analysis has been saved successfully.
# Important

# Do not parse or modify the Gemini response yet.

# The flow is:

# support_feedback
#        ↓
#    Gemini API
#        ↓
#  response.text
#        ↓
# support_feedback_analysis.txt
# Goal

# Practice API Response → String → File Writing.

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

with open("support_feedback_analysis.txt","w") as w_file:
    w_file.write(str(gemini_response_list))

print("AI analysis has been saved successfully.")
# for re in gemini_response_list:
#     print(re)