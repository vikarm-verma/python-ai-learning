# Import the Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig


# Create Gemini configuration
gemini = GeminiConfig()


# Create Gemini language model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Function to rewrite the user's question
def rewrite_query(question, conversation):

    prompt = f"""
Rewrite the user's question into a clear, standalone search query.

Use the conversation context to understand references such as
"those", "it", "they", or similar words.

Do not answer the question.
Only return the rewritten search query.

Conversation:
{conversation}

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()


# Run this file directly for testing
if __name__ == "__main__":

    question = input("Enter your question: ")

    conversation = """
User: How many annual leave days are employees eligible for?
Assistant: Employees are eligible for 20 days of annual leave in a calendar year.
"""

    rewritten_query = rewrite_query(
        question,
        conversation
    )

    print("\n--- Original Question ---")
    print(question)

    print("\n--- Rewritten Query ---")
    print(rewritten_query)