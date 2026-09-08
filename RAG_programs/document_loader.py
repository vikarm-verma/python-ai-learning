    # Import PyPDFLoader to read and extract content from PDF files
from langchain_community.document_loaders import PyPDFLoader
# Run the code below only when this Python file is executed directly,
# not when it is imported by another Python file

    
# Define the path of the PDF file that we want to load
pdf_path = "messy_company_hr_policy.pdf"

# Create a loader object for the specified PDF file
loader = PyPDFLoader(pdf_path)

# Load the PDF and convert its pages into LangChain Document objects
documents = loader.load()

if __name__ == "__main__":
    # Display the number of pages/documents loaded from the PDF
    print("Total pages loaded:", len(documents))

    # Display the extracted text from the first page
    print("\n--- First Page Content ---")
    print(documents[0].page_content)

    # Display the metadata associated with the first page
    print("\n--- First Page Metadata ---")
    print(documents[0].metadata)