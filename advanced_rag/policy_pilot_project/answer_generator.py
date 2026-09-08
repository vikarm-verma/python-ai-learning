from langchain_google_genai import ChatGoogleGenerativeAI
from shared.gemini_config import GeminiConfig


# Load Gemini configuration
gemini = GeminiConfig()


# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


def generate_answer(query, compressed_context):

    context = "\n\n".join(compressed_context)

    prompt = f"""
You are an HR policy assistant.

Answer the user's question using only the provided context.

User Question:
{query}

Context:
{context}

Rules:
- Use only the information provided in the context.
- Do not invent or assume information.
- If the context does not contain the answer, say:
"I could not find this information in the provided HR policy."
- Give a clear and concise answer.

Answer:
"""

    response = llm.invoke(prompt)

    return response.content.strip()


if __name__ == "__main__":

    query = input("Enter your question: ")

    # Sample compressed context for testing
    compressed_context = [
        "Employees are eligible for 20 days of annual leave in a calendar year."
    ]

    answer = generate_answer(
        query,
        compressed_context
    )

    print("\n--- Final Answer ---")
    print(answer)