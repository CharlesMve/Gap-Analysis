import pymupdf4llm
import pymupdf
from llama_index.core import Document

md_read = pymupdf4llm.LlamaMarkdownReader()
data = md_read.load_data("C:\\Users\\20029822\\Documents\\Gap Analysis\\Navistar DR100159-06.pdf")

print(data[29].get_content())