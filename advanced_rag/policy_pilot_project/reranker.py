from langchain_google_genai import ChatGoogleGenerativeAI
from shared.gemini_config import GeminiConfig
from RAG_programs.vector_store import vector_store


# Gemini configuration
gemini = GeminiConfig()


# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)


def rerank_documents(query, documents):

    prompt = f"""
You are a document reranker.

User Query:
{query}

Below are retrieved documents.

Rank these documents from most relevant to least relevant
for answering the user query.

Return ONLY the document numbers in this format:
3,1,5,2,4

Documents:
"""

    for i, doc in enumerate(documents, 1):
        prompt += f"""

Document {i}:
{doc.page_content}
"""

    response = llm.invoke(prompt)

    ranking = response.content.strip()

    print("\n--- Reranker Ranking ---")
    print(ranking)

    ranked_documents = []

    for number in ranking.split(","):
        number = int(number.strip())
        ranked_documents.append(documents[number - 1])

    return ranked_documents


# Run this program directly
if __name__ == "__main__":

    query = input("Enter your question: ")

    print("\n--- Original Query ---")
    print(query)

    # Retrieve documents
    documents = retriever.invoke(query)

    print("\n--- Retrieved Documents ---")

    for i, doc in enumerate(documents, 1):
        print(f"\nDocument {i}:")
        print(doc.page_content)

    # Rerank documents
    ranked_documents = rerank_documents(
        query,
        documents
    )

    print("\n--- Reranked Documents ---")

    for i, doc in enumerate(ranked_documents, 1):
        print(f"\nRank {i}:")
        print(doc.page_content)