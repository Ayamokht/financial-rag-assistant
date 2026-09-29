def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[str]:

    """
    Split text into overlapping chunks. 
    - overlap pour garder le contexte en splittant les phrases ..  
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks

def chunk_pages(
    pages: list[dict],
    source: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[dict]:

    """
    Split document pages into chunks while preserving metadata.
    """

    all_chunks = []

    chunk_id = 0

    for page in pages:

        page_chunks = split_text(
            page["text"],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        for chunk in page_chunks:

            all_chunks.append({
                "chunk_id": chunk_id,
                "source": source,
                "page": page["page"],
                "text": chunk
            })

            chunk_id += 1

    return all_chunks

if __name__ == "__main__":

    from document_loader import load_pdf

    PDF_PATH = "data/raw/bnp_paribas_annual_report_2025.pdf"

    pages = load_pdf(PDF_PATH)

    chunks = chunk_pages(
        pages=pages,
        source="bnp_paribas_annual_report_2025.pdf"
    )

    print("Nombre de pages :", len(pages))
    print("Nombre de chunks :", len(chunks))

    print("\nPremier chunk :")
    print(chunks[0])


# PDF BNP — 936 pages
#        ↓
#     PyMuPDF
#        ↓
#   load_pdf()
#        ↓
# pages + métadonnées
#        ↓
#   split_text()
#        ↓
#   chunk_pages()
#       ↓
# chunks + métadonnées
#        ↓
#   EMBEDDINGS  
#        ↓
# Vector Store
#        ↓
#   Retrieval
#        ↓
#      LLM