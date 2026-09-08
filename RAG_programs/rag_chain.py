# Import the retriever created from the vector store
from retriever import retriever

# Import the Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig

# Import ChatPromptTemplate to create a reusable prompt template
from langchain_core.prompts import ChatPromptTemplate

# Import StrOutputParser to convert the model response into plain text
from langchain_core.output_parsers import StrOutputParser


# Create a Gemini configuration object
# This loads the GEMINI_API_KEY from the .env file
gemini = GeminiConfig()


# Create the Gemini language model
# The model will generate the final answer using the retrieved context
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Create a prompt template for the RAG application
# The template will receive the retrieved context and user's question
prompt = ChatPromptTemplate.from_template("""
You are an HR policy assistant.

Answer the question using only the information provided in the context.

If the answer is not present in the context, say:
"I could not find this information in the provided HR policy."

Context:
{context}

Question:
{question}

Answer:
""")


# Create an output parser
# This converts the AIMessage returned by Gemini into plain text
output_parser = StrOutputParser()


# Ask the user to enter a question
# This makes the application interactive
question = input("\nEnter your question: ")


# Retrieve the relevant document chunks
# The retriever searches the vector store using the user's question
relevant_chunks = retriever.invoke(question)


# Combine the retrieved chunks into one context string
# This context will be passed to the prompt
context = "\n\n".join(
    chunk.page_content for chunk in relevant_chunks
)


# Create the RAG chain
# The prompt receives context and question, then sends them to Gemini,
# and the output parser converts the response into plain text
rag_chain = prompt | llm | output_parser


# Run the chain with the retrieved context and user's question
# The chain executes prompt → LLM → output parser in sequence
answer = rag_chain.invoke({
    "context": context,
    "question": question
})


# Display the final answer
print("\n--- RAG Answer ---")
print(answer)