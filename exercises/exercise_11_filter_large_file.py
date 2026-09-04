# Exercise 11 — Filter a Large File

# File: exercise_11_filter_large_file.py

# Use Case

# You have a customer feedback file containing 10,000 lines. You want to remove all feedback entries that mention:

# The delivery was very late.
# Task
# Open customer_feedback_10000.txt in read mode.
# Create a new file named customer_feedback_filtered.txt.
# Read the original file one line at a time.
# If a line contains "The delivery was very late.", skip that line.
# Write all other lines to the new file.
# Count how many lines remain in the filtered file.
# Print the total number of remaining lines.
# Important Constraints
# Do not use readlines().
# Do not load the entire file into a list.
# Process the file line by line.
# Do not modify the original file.
# Expected Output
# Total remaining lines: 9000
# Goal

# Practice large-file processing, file reading, file writing, filtering, loops, if, continue, and counters.
original=0
filtered=0

with open("../python-basics-of-ai/customer_feedback_10000.txt","r")as r_file:
    with open("../python-basics-of-ai/customer_feedback_filtered.txt","w")as w_file:
        for line in r_file:
            # print(line)
            original=original+1
            if "The delivery was very late." in line:
                continue
            w_file.write(line)
            filtered= filtered+1
            
print(f"""original file carries line: {original}\nfiltered file carries lines: {filtered}""")
        