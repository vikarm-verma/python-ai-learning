# Import the existing retriever from the vector store
from retriever import retriever

# Import the tool decorator
from langchain_core.tools import tool

# Import the Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI

# Import the Gemini configuration class
from shared.gemini_config import GeminiConfig

# Import create_agent to create the LangChain agent
from langchain.agents import create_agent


# Create a Gemini configuration object
# This loads the GEMINI_API_KEY from the .env file
gemini = GeminiConfig()


# Create the Gemini language model
# The agent will use Gemini to reason and generate responses
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini.api_key
)


# Create a tool for searching the HR policy
# The agent can decide when this tool is required
@tool
def search_hr_policy(query: str) -> str:
    """Search the company HR policy for relevant information."""

    # Retrieve relevant chunks from the vector store
    relevant_chunks = retriever.invoke(query)

    # Convert the retrieved chunks into a single text response
    return "\n\n".join(
        chunk.page_content for chunk in relevant_chunks
    )


# Create the agent
# The agent can decide when to use the HR policy search tool
agent = create_agent(
    model=llm,
    tools=[search_hr_policy],
    system_prompt="""
 Use the search_hr_policy tool when the question is related to the HR policy.

For general questions that are not related to the HR policy,
answer using your general knowledge.

Do not use the HR policy tool for unrelated questions.
    """
)


# Create a list to store the conversation messages
# The same message history will be sent to the agent on every turn
messages = []


# Start a continuous conversation
# The loop keeps asking questions until the user types exit
while True:

    # Ask the user for the next question
    question = input("\nYou: ")

    # Stop the conversation when the user types exit
    if question.lower() == "exit":
        print("\nConversation ended.")
        break

    # Add the user's question to the conversation history
    # This allows the agent to see previous questions and answers
    messages.append({
        "role": "user",
        "content": question
    })


    # Send the complete conversation to the agent
    # The agent can use previous messages to understand follow-up questions
    result = agent.invoke({
        "messages": messages
    })


    # Update the conversation history with the agent's response
    # This preserves the agent's previous response for the next question
    messages = result["messages"]


    # Get the latest message from the agent
    # This is the agent's final response for the current question
    answer = messages[-1].content


    # Gemini may return structured content instead of plain text
    # Extract only the actual text from the response
    if isinstance(answer, list):
        answer = "".join(
            item["text"]
            for item in answer
            if isinstance(item, dict) and item.get("type") == "text"
        )


    # Display the agent's answer
    print("\nAgent:", answer)