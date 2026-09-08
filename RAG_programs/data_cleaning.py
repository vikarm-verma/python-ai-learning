# Import the documents loaded by the document loader
from document_loader import documents

# Import the regular expression module for pattern-based text cleaning
import re




# Define a function to clean the extracted text
def clean_text(text):

    # Remove page numbers such as "Page 1", "Page 2", etc.
    text = re.sub(r"Page\s*\d+", "", text)

    # Remove the HR department label that appears in the PDF header
    text = re.sub(r"HR\s+Department", "", text)
    
    # Remove the repeated company policy header
    text = re.sub(r"ACME\s+COMPANY\s+HR\s+POLICY", "", text)

    # Remove the confidentiality label wherever it appears
    text = re.sub(r"\bCONFIDENTIAL\b", "", text)

    # Remove repeated note labels while keeping the actual sentence
    text = re.sub(r"NOTE\s+NOTE:\s*", "", text)

    # Remove the end-of-policy marker
    text = re.sub(r"END\s+OF\s+POLICY", "", text)

    # Remove decorative asterisks
    text = re.sub(r"\*+", "", text)

    # Remove leftover pipe characters
    text = re.sub(r"\|", "", text)

    # Remove a trailing hyphen left by the footer
    text = re.sub(r"\s+-\s*$", "", text)

    # Replace multiple spaces and line breaks with a single space
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary spaces from the beginning and end
    return text.strip()


# Clean the content of every document
for document in documents:

    # Replace the original content with the cleaned content
    document.page_content = clean_text(document.page_content)

# Run the code below only when this Python file is executed directly,
# not when it is imported by another Python file
if __name__ == "__main__":
    
    # Display the cleaned pages for verification
    for index, document in enumerate(documents):

        # Display the page number
        print(f"\n--- Cleaned Page {index + 1} ---")

        # Display the cleaned content
        print(document.page_content)