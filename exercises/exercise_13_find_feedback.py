# Exercise 13 — Find Specific Feedback

# File: exercise_13_find_feedback.py

# Use Case

# You have loaded customer feedback into a Python list. Now, you want to find all feedback entries that contain the word "support".

# Task
# Read customer_feedback_filtered.txt line by line.
# Store each line in a list called feedback.
# Create an empty list called support_feedback.
# Loop through the feedback list.
# Check whether "support" is present in each feedback entry.
# If it is present, add that entry to support_feedback.
# Print:
# The total number of matching feedback entries.
# The matching feedback entries.
# Expected Output
# Support feedback: 1000

# Feedback 3: Customer support was helpful.
# Feedback 13: Customer support was helpful.
# ...
# Constraints
# Do not use readlines().
# Use for, if, in, and .append().
# Do not modify the original file.
# Goal

# Practice:

# File → List → Loop → Search → Filter → New List


with open("../python-basics-of-ai/customer_feedback_filtered.txt","r")as r_file:
    feedback=[]
    support_feedback=[]
    matching_feedback=0
    for line in r_file:
        if "support" in line:
            support_feedback.append(line)
            print(line)
            matching_feedback+=1
    # this is not optimal approach 
    #     feedback.append(line)
    # for fb in feedback:
    #     if "support" in fb:
    #         support_feedback.append(fb)
    #         matching_feedback+=1
# for sf in support_feedback:
#     print(sf)       
print(f"total matching feedback :{matching_feedback}")

            

 