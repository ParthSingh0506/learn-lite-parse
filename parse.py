import pdfplumber
from pypdf import PdfReader
from liteparse import LiteParse
import ollama
import time

PDF_PATH = "wipo_pub_rn2021_18e.pdf"
PAGE_NUM = 23
QUESTION = "What is the total assets of WIPO as at December 31, 2020?"

def extract_pypdf():
    reader = PdfReader(PDF_PATH)
    return reader.pages[PAGE_NUM].extract_text()

def extract_pdfplumber():
    with pdfplumber.open(PDF_PATH) as pdf:
        return pdf.pages[PAGE_NUM].extract_text()

def extract_liteparse():
    parser = LiteParse()
    result = parser.parse(PDF_PATH, target_pages=str(PAGE_NUM + 1))
    return result.text

def ask_llm(context):
    response = ollama.chat(
        model="gemma4:e4b",          # ← changed
        options={"temperature": 0}, # ← deterministic answers, better for benchmarking
        messages=[{
            "role": "user",
            "content": f"""You are a financial document assistant. Answer the question based ONLY on the document provided.
             If the answer is not in the document, say "Answer not found in document."

Question: {QUESTION}

Document:
{context}

Return only the direct answer, no explanation."""
        }]
    )
    return response['message']['content'].strip()

def run(method_name, fn):
    start = time.time()
    text = fn()
    print('text is:-',text)
    parse_time = time.time() - start

    start = time.time()
    answer = ask_llm(text)
    inference_time = time.time() - start

    print(f"\n--- {method_name} ---")
    print(f"Answer:         {answer}")
    print(f"Parsing Time:   {parse_time:.2f}s")
    print(f"Inference Time: {inference_time:.2f}s")

run("PyPDF",      extract_pypdf)
run("pdfplumber", extract_pdfplumber)
run("LiteParse",  extract_liteparse)