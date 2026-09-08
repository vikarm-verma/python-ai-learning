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
# The model will generate the final answer from the retrieved context
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Ask the user to enter a question
# This makes the RAG application interactive
question = input("\nEnter your question: ")


# Retrieve the most relevant chunks from the vector store
# The retriever searches for information related to the user's question
relevant_chunks = retriever.invoke(question)


# Combine the retrieved chunks into a single context
# This context will be passed to Gemini
context = "\n\n".join(
    chunk.page_content for chunk in relevant_chunks
)


# Create a prompt using the retrieved context and user question
# Gemini is instructed to answer only from the retrieved information
prompt = f"""
You are an HR policy assistant.

Answer the question using only the information provided in the context.
If the answer is not present in the context, say:
"I could not find this information in the provided HR policy."

Context:
{context}

Question:
{question}

Answer:
"""


# Send the prompt to Gemini
# Gemini generates the final answer using the retrieved context
response = llm.invoke(prompt)


# Display the final answer
print("\n--- RAG Answer ---")
print(response.content)