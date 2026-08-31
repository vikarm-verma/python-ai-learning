from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

# feedback = input("Enter Customer feedback :")

feedbacks = [
    "Product is excellent",
    "Delivery was late",
    "Customer support was helpful",
    "The product quality is poor"
]


# answer = response.text
# print(f"answer is :{answer}")

results=[]

for feedback in feedbacks: 
    prompt = f"""
    Classify this customer feedback.
    Return ONLY one word:
    Positive or Negative

    Feedback:
    {feedback}
    """
    response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents = prompt
        )


    # if "Positive" in response.text:
    #     print("No immediate action required")
    # else:
    #     print("Customer support should contact the customer")
    # print(f"Gemini says: {response.text}")

    answer = response.text.strip()

    results.append(answer)

    

print(results)