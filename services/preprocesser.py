import io
import pandas as pd
import fitz  # PyMuPDF
import docx
async def parse_uploaded_files(files):
    documents = []
    for file in files:
        content = await file.read()
        filename = file.filename.lower()
        if filename.endswith(".pdf"):
            doc = fitz.open(stream=content, filetype="pdf")
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text()
                documents.append({"text": text, "page": page_num + 1, "filename": file.filename})
        elif filename.endswith(".docx"):
            doc = docx.Document(io.BytesIO(content))
            text = "\n".join([para.text for para in doc.paragraphs])
            documents.append({"text": text, "page": 1, "filename": file.filename})
        elif filename.endswith(".txt"):
            text = content.decode("utf-8")
            documents.append({"text": text, "page": 1, "filename": file.filename})
        else:
            continue
    return documents


def clean_text(text):
    return " ".join(text.split())

def chunk_documents(docs, chunk_size=300):
    chunks = []
    for doc in docs:
        words = doc["text"].split()
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i+chunk_size])
            chunks.append({
                "text": chunk,
                "page": doc["page"]
            })
    return chunks