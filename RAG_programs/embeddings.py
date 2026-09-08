# Import the chunks created by the text splitter
from text_splitter import chunks

# Import the Gemini embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig


# Run the code below only when this Python file is executed directly,
# not when it is imported by another Python file


# Create a Gemini configuration object
# The class loads the API key from the .env file
gemini = GeminiConfig()


# Create the Gemini embedding model
# The API key is accessed through the configuration object
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=gemini.api_key
)


# Select the first chunk for testing
first_chunk = chunks[0].page_content


# Convert the chunk into an embedding vector
first_vector = embedding_model.embed_query(first_chunk)

if __name__ == "__main__":
    # Display the original chunk
    print("\n--- Original Chunk ---")
    print(first_chunk)


    # Display the generated vector
    print("\n--- Embedding Vector ---")
    print(first_vector)


    # Display the number of dimensions
    print("\n--- Vector Dimensions ---")
    print(len(first_vector))