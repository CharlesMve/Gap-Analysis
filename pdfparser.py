import os
import requests
import pymupdf4llm
from dotenv import load_dotenv
from llama_index.core import Document
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage
from google import genai
import tkinter as tk
from tkinter import filedialog

load_dotenv()


def get_LLM_response(prompt):
    llm = GoogleGenAI(
        model="gemini-2.0-flash",
        api_key=os.getenv("API_KEY"),
    )


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
    print("Select OE Document: ")
    OE_PDF = get_PDF_file()
    print(OE_PDF,"\n")

    print("Select Bendix Document: ")
    Bendix_PDF = get_PDF_file()
    print(Bendix_PDF,"\n")

    #Load and parse the PDF files
    pdf_reader = pymupdf4llm.LlamaPDFReader()
    OE_data = pdf_reader.load_data(OE_PDF)
    Bendix_data = pdf_reader.load_data(Bendix_PDF)

    #Print the content of the 30th page
    if len(data) >= 30:
        print(data[29].get_content())
    else:
       print("The selected PDF has less than 30 pages.")