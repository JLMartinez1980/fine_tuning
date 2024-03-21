import PyPDF2
import json
import os

# Set the directory path to your specified folder on the desktop
directory_path = '/Users/jamesmartinez/Desktop/PDFs'

# Iterate over all files in the specified directory
for filename in os.listdir(directory_path):
    if filename.endswith(".pdf"):  # Check if the file is a PDF
        pdf_file_path = os.path.join(directory_path, filename)
        
        # Open and read the PDF file using PdfReader
        with open(pdf_file_path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            
            # Define the JSONL file path (same name as the PDF but with .jsonl extension)
            jsonl_file_path = os.path.join(directory_path, f"{os.path.splitext(filename)[0]}.jsonl")
            
            # Open the JSONL file for writing
            with open(jsonl_file_path, 'w') as jsonl_file:
                for page_num in range(len(pdf.pages)):
                    page = pdf.pages[page_num]
                    text = page.extract_text() + "\n"  # Extract text from each page
                    # Ensure the text is not just whitespace
                    if text.strip():  
                        # Structure each page as a separate dictionary
                        data = {
                            "documentTitle": filename,
                            "page": page_num + 1,  # Page numbering starts at 1
                            "content": text.strip()
                        }
                        # Convert the dictionary to a JSON string and write it to the JSONL file
                        jsonl_str = json.dumps(data) + "\n"  # Convert data to JSON string and add newline
                        jsonl_file.write(jsonl_str)

        print(f"Processed {filename} into JSONL")
