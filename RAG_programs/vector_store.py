# Import the chunks created by the text splitter
from text_splitter import chunks

# Import the Gemini embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Import Chroma as the vector store
from langchain_chroma import Chroma

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig


# Create a Gemini configuration object
# This loads the GEMINI_API_KEY from the .env file
gemini = GeminiConfig()


# Create the Gemini embedding model
# This model converts each document chunk into a numerical vector
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=gemini.api_key
)


# Create the Chroma vector store from the document chunks
# Chroma automatically creates embeddings and stores the chunks with their vectors
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="company_hr_policy"
)


# Run the following code only when this file is executed directly
# This prevents these print statements from running when vector_store is imported
if __name__ == "__main__":

    # Display a confirmation that the vector store was created
    print("Vector store created successfully.")

    # Display the number of chunks stored in the vector store
    print("Chunks stored:", len(chunks))