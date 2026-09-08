from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from shared.gemini_config import GeminiConfig


# Load Gemini configuration
gemini = GeminiConfig()


# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


def compress_documents(query, documents):

    compressed_documents = []

    for i, doc in enumerate(documents, 1):

        prompt = f"""
You are a context compressor for a RAG system.

User Query:
{query}

Document:
{doc.page_content}

Task:
Extract only the information from this document that is directly
useful for answering the user query.

Rules:
- Keep only relevant information.
- Remove irrelevant information.
- Do not add information that is not present in the document.
- If the document has no relevant information, return exactly:
NOT RELEVANT

Return only the compressed relevant information.
"""

        response = llm.invoke(prompt)

        content = response.content.strip()

        if content != "NOT RELEVANT":
            compressed_documents.append(content)

    return compressed_documents


# Run this file directly
if __name__ == "__main__":

    query = input("Enter your question: ")

    print("\n--- Original Query ---")
    print(query)

    # Sample documents for testing
    documents = [
        Document(
            page_content=(
                "Employees are eligible for 20 days of annual leave "
                "in a calendar year."
            )
        ),
        Document(
            page_content=(
                "Employees must submit leave requests through "
                "the HR portal."
            )
        ),
        Document(
            page_content=(
                "The company provides medical insurance to "
                "eligible employees."
            )
        )
    ]

    # Compress the documents
    compressed = compress_documents(
        query,
        documents
    )

    print("\n--- Compressed Context ---")

    if not compressed:
        print("No relevant information found.")
    else:
        for i, content in enumerate(compressed, 1):
            print(f"\nContext {i}:")
            print(content)