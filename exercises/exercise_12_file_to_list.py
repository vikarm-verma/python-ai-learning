# Exercise 12 — Load Filtered Data into a List

# File: exercise_12_file_to_list.py

# Use Case

# You have already filtered the customer feedback and stored the results in customer_feedback_filtered.txt. Now you want to load the remaining feedback into a Python list so it can be processed further.

# Task
# Open customer_feedback_filtered.txt in read mode.
# Create an empty list called feedback.
# Read the file line by line.
# Add each line to the feedback list using .append().
# Print:
# The total number of feedback entries.
# The first feedback entry.
# The last feedback entry.
# Expected Output
# Total feedback: 9000
# First feedback: The product quality is excellent.
# Last feedback: ...

# The exact last feedback will depend on the generated file.

# Constraint

# For this exercise, do not use readlines(). Practice building the list yourself using:

# for line in file:

# and:

# feedback.append(line)
# Goal

# Practice moving data from:

# Text File → Python List → Data Processing

with open("../python-basics-of-ai/customer_feedback_filtered.txt","r")as r_file:
    feedback=[]
    total_feedback=0;
    first_feeback=''
    last_feedback=''
    for line in r_file:
        feedback.append(line)
        total_feedback=total_feedback+1;
    first_feeback=feedback[0]
    last_feedback=feedback[total_feedback-1]

print(f"""
      Total Feedback : {total_feedback}
      First Feedback : {first_feeback}
      Last  Feedback : {last_feedback}
      """)    
 
            
# print(f"""original file carries line: {original}\nfiltered file carries lines: {filtered}""")
        