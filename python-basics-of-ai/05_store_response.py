from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

question = input("Ask Gemini :")

prompt =f"""
You are a Python teacher.
Explain the following topic in simple language with one example:
{question}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = prompt
)
answer = response.text
print(f"Gemini says: {answer}")