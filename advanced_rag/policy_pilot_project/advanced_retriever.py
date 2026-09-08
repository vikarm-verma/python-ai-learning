# Import the query rewriter
# This converts the user's question into a better search query
from query_rewriter import llm

import sys

# # # Add RAG_programs to Python's module search path
# # # __file__ points to advanced_retriever.py
# sys.path.append("../../RAG_programs")

# Import the existing vector store
# This is the Chroma vector store containing our HR policy chunks
from vector_store import vector_store



# Get the user's original question
question = input("Enter your question: ")


# Create the prompt for query rewriting
# The model will convert the question into a standalone search query
prompt = f"""
Rewrite the following user question into a clear search query
for retrieving relevant information from an HR policy document.

Do not answer the question.
Return only the rewritten search query.

User Question:
{question}
"""


# Send the question to Gemini for rewriting
response = llm.invoke(prompt)


# Get the rewritten query from Gemini's response
rewritten_query = response.content.strip()


# Display the original question
print("\n--- Original Question ---")
print(question)


# Display the rewritten query
print("\n--- Rewritten Query ---")
print(rewritten_query)


# Search the vector store using the rewritten query
# The retriever finds the chunks most similar to the rewritten query
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)


# Retrieve the most relevant chunks
retrieved_chunks = retriever.invoke(rewritten_query)


# Display the retrieved chunks
print("\n--- Retrieved Chunks ---")

for i, chunk in enumerate(retrieved_chunks, start=1):

    print(f"\n--- Chunk {i} ---")
    print(chunk.page_content)

    print("\nMetadata:")
    print(chunk.metadata)