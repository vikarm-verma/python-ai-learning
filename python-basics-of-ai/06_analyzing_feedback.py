from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

feedback = input("Enter Customer feedback :")

prompt =f"""
Analyze this customer feedback and classify it as positive or Negative.
{feedback}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = prompt
)
answer = response.text
print(f"answer is :{answer}")

if "Positive" in answer:
    print("No immediate action required")
else:
    print("Customer support should contact the customer")
# print(f"Gemini says: {answer}")
