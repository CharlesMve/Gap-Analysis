import pymupdf4llm
import pymupdf
from dotenv import load_dotenv
from llama_index.core import Document
from google import genai
import requests
import os
import tkinter as tk
from tkinter import filedialog

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

def get_LLM_response(prompt):
    pass

def get_PDF_file():
# Prompt user to select a PDF file
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not pdf_path:
        print("No file selected.")
        exit()
    return pdf_path


if __name__ == "__main__":
    # Prompt user to select a PDF file
    example_pdf = get_PDF_file

    print('\n***Example output for the LLM***\n')
    # Load the PDF file
    pdf_reader = pymupdf4llm.LlamaPDFReader()
    data = pdf_reader.load_data(example_pdf)

    # Print the content of the 30th page
    if len(data) >= 30:
        print(data[29].get_content())
    else:
        print("The selected PDF has less than 30 pages.")