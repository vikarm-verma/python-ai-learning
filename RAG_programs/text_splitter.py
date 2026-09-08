# Import the cleaned documents from the previous program
from data_cleaning import documents

# Import RecursiveCharacterTextSplitter to divide large documents into smaller chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Run the code below only when this Python file is executed directly,
# not when it is imported by another Python file


# Create a text splitter with a target chunk size of 500 characters
# A smaller chunk makes it easier for the retriever to find specific information
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,

    # Keep 50 characters from the previous chunk in the next chunk
    # This helps preserve context when an important sentence crosses a chunk boundary
    chunk_overlap=50
)


# Split the cleaned documents into smaller chunks
chunks = splitter.split_documents(documents)

if __name__ == "__main__":
    # Display the total number of chunks created
    # This helps us understand how the document was divided
    print("Total chunks:", len(chunks))


    # Display each chunk so we can inspect the result of the splitting process
    for index, chunk in enumerate(chunks):

        # Print the chunk number for easier identification
        print(f"\n--- Chunk {index + 1} ---")

        # Print the actual text stored inside the chunk
        print(chunk.page_content)

        # Print the metadata to verify that source/page information is preserved
        print("Metadata:", chunk.metadata)