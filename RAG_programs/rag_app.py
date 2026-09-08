# Import the retriever created from the vector store
from retriever import retriever

# Import the Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig


# Create a Gemini configuration object
# This loads the GEMINI_API_KEY from the .env file
gemini = GeminiConfig()


# Create the Gemini language model
# The model will generate the final answer using the retrieved context
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Define the user's question
question = "How many annual leave days are employees eligible for?"


# Retrieve relevant document chunks using the user's question
# The retriever searches the vector store for semantically relevant information
relevant_chunks = retriever.invoke(question)


# Combine the retrieved chunks into a single context string
# This context will be provided to the language model
context = "\n\n".join(
    chunk.page_content for chunk in relevant_chunks
)


# Create a prompt containing the retrieved context and user's question
# The model is instructed to answer only using the provided context
prompt = f"""
You are an HR policy assistant.

Answer the user's question using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""


# Send the prompt to Gemini
# Gemini uses the retrieved document context to generate the answer
response = llm.invoke(prompt)


# Display the user's question
print("\n--- User Question ---")
print(question)


# Display the final RAG-generated answer
print("\n--- RAG Answer ---")
print(response.content)