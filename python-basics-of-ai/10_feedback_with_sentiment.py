from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Multiple customer feedbacks
feedbacks = [
    "Product is excellent.",
    "Delivery was very late.",
    "Customer support was very helpful.",
    "The product quality is poor."
]

# Store results
results = []

# Analyze each feedback
for feedback in feedbacks:

    prompt = f"""
    Classify this customer feedback as Positive or Negative.

    Return ONLY one word:
    Positive
    or
    Negative

    Feedback:
    {feedback}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text.strip()

    # Store feedback and its sentiment together
    results.append({
        "feedback": feedback,
        "sentiment": answer
    })

# Display results
for result in results:
    print("Feedback:", result["feedback"])
    print("Sentiment:", result["sentiment"])
    print()