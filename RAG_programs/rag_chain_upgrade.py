# Import the retriever created from the vector store
from retriever import retriever

# Import the Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig

# Import the prompt template
from langchain_core.prompts import ChatPromptTemplate

# Import StrOutputParser to convert the model response into plain text
from langchain_core.output_parsers import StrOutputParser

# Import RunnablePassthrough to pass the original question through the chain
from langchain_core.runnables import RunnablePassthrough


# Create a Gemini configuration object
# This loads the GEMINI_API_KEY from the .env file
gemini = GeminiConfig()


# Create the Gemini language model
# Gemini will generate the final answer using the retrieved context
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Create a prompt template
# The context and question will be supplied by the chain
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
# This converts Gemini's response into plain text
output_parser = StrOutputParser()


# Create the complete RAG chain
# The retriever receives the question and returns relevant documents
# The retrieved documents are converted into a text context
# The original question is passed directly to the prompt
# The prompt then goes to Gemini, and the parser extracts the final text
rag_chain = (
    {
        "context": retriever | (lambda docs: "\n\n".join(
            doc.page_content for doc in docs
        )),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | output_parser
)


# Ask the user to enter a question
question = input("\nEnter your question: ")


# Run the complete RAG chain
# The question flows through retrieval, prompt, Gemini, and output parsing
answer = rag_chain.invoke(question)


# Display the final answer
print("\n--- RAG Answer ---")
print(answer)