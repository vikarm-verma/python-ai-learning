# Import itemgetter to extract the question from the input dictionary
from operator import itemgetter

# Import the retriever created from the vector store
from retriever import retriever

# Import the Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig

# Import the prompt template
from langchain_core.prompts import ChatPromptTemplate

# Import the output parser
from langchain_core.output_parsers import StrOutputParser

# Import RunnablePassthrough to pass the current question through the chain
from langchain_core.runnables import RunnablePassthrough

# Import RunnableWithMessageHistory to add conversation memory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Import in-memory chat history
from langchain_core.chat_history import InMemoryChatMessageHistory


# Create a Gemini configuration object
# This loads the GEMINI_API_KEY from the .env file
gemini = GeminiConfig()


# Create the Gemini language model
# Gemini will generate the final answer using the retrieved context
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Create the prompt template
# The prompt receives the question, retrieved context, and conversation history
prompt = ChatPromptTemplate.from_template("""
You are an HR policy assistant.

Use the provided context and conversation history to answer the user's question.

Answer using only information available in the HR policy context.

If the answer is not present in the context, say:
"I could not find this information in the provided HR policy."

Conversation History:
{chat_history}

Context:
{context}

Question:
{question}

Answer:
""")


# Create an output parser
# This converts Gemini's response into plain text
output_parser = StrOutputParser()


# Create a function to convert retrieved documents into plain text
# This combines all retrieved chunks into one context string
def format_documents(documents):

    # Join the content of all retrieved documents
    return "\n\n".join(
        document.page_content for document in documents
    )


# Create the RAG chain
# itemgetter("question") sends only the question to the retriever
# The retriever returns relevant documents
# format_documents converts those documents into context
# RunnablePassthrough passes the original question forward
rag_chain = (
    {
        "context": itemgetter("question") | retriever | format_documents,
        "question": itemgetter("question"),
        "chat_history": itemgetter("chat_history")
    }
    | prompt
    | llm
    | output_parser
)


# Create a dictionary to store conversation histories
# Each session can maintain its own separate conversation
store = {}


# Create a function that returns the history for a session
def get_session_history(session_id):

    # Create a new history if this session does not exist
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    # Return the conversation history for this session
    return store[session_id]


# Add conversation memory to the RAG chain
# LangChain will automatically manage previous messages for the session
rag_with_memory = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="chat_history"
)


# Define the session ID
# Questions and answers in the same session share the same memory
session_id = "hr_policy_session"


# Start the interactive chat
while True:

    # Ask the user for a question
    question = input("\nYou: ")

    # Stop the application when the user types exit
    if question.lower() == "exit":
        break

    # Run the RAG chain with memory
    # The session ID tells LangChain which conversation history to use
    answer = rag_with_memory.invoke(
        {"question": question},
        config={
            "configurable": {
                "session_id": session_id
            }
        }
    )

    # Display the generated answer
    print("\nAI:", answer)