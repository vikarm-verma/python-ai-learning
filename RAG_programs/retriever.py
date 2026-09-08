# Import the vector store created in the previous program
from vector_store import vector_store


# Create a retriever from the vector store
# The retriever will search for document chunks relevant to a user query
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# Define a question that we want to search for
query = "How many annual leave days are employees eligible for?"


# Retrieve the most relevant chunks for the query
# The retriever converts the query into an embedding and finds similar vectors
relevant_chunks = retriever.invoke(query)

# Run the code below only when this Python file is executed directly,
# not when it is imported by another Python file
if __name__ == "__main__":

    # Display the user's query
    print("\n--- User Query ---")
    print(query)


    # Display the retrieved chunks
    print("\n--- Retrieved Chunks ---")

    for index, chunk in enumerate(relevant_chunks):

        # Display the retrieved chunk number
        print(f"\n--- Retrieved Chunk {index + 1} ---")

        # Display the chunk's actual text
        print(chunk.page_content)

        # Display the source metadata
        print("Metadata:", chunk.metadata)