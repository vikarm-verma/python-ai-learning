# Import query rewriter
from query_rewriter import rewrite_query

# Import vector store
from RAG_programs.vector_store import vector_store

# Import reranker
from reranker import rerank_documents

# Import context compressor
from context_compressor import compress_documents

# Import answer generator
from answer_generator import generate_answer


if __name__ == "__main__":

    # Step 1: Get the user's question
    original_query = input("Enter your question: ")

    print("\n--- Original Question ---")
    print(original_query)


    # Step 2: Previous conversation
    # This provides context for follow-up questions.
    conversation = """
User: How many annual leave days are employees eligible for?
Assistant: Employees are eligible for 20 days of annual leave in a calendar year.
"""


    # Step 3: Rewrite the question
    rewritten_query = rewrite_query(
        original_query,
        conversation
    )

    print("\n--- Rewritten Query ---")
    print(rewritten_query)


    # Step 4: Retrieve documents
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 5}
    )

    documents = retriever.invoke(rewritten_query)

    print("\n--- Retrieved Documents ---")

    for i, doc in enumerate(documents, 1):
        print(f"\nDocument {i}:")
        print(doc.page_content)


    # Step 5: Rerank documents
    ranked_documents = rerank_documents(
        rewritten_query,
        documents
    )

    print("\n--- Reranked Documents ---")

    for i, doc in enumerate(ranked_documents, 1):
        print(f"\nRank {i}:")
        print(doc.page_content)


    # Step 6: Compress the context
    compressed_context = compress_documents(
        rewritten_query,
        ranked_documents
    )

    print("\n--- Compressed Context ---")

    for i, context in enumerate(compressed_context, 1):
        print(f"\nContext {i}:")
        print(context)


    # Step 7: Generate the final answer
    final_answer = generate_answer(
        original_query,
        compressed_context
    )

    print("\n--- Final Answer ---")
    print(final_answer)