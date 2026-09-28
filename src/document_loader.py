# ============================================================
# PIPELINE D'EXTRACTION DU DOCUMENT
# ============================================================
#
# PDF
#  ↓
# pymupdf.open()
#  ↓
# Document
#  ↓
# document[0]
#  ↓
# Page
#  ↓
# page.get_text()
#  ↓
# str (texte)
#
# ============================================================

import pymupdf


def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF while preserving page metadata.

    Args:
        file_path: Path to the PDF file.

    Returns:
        A list of dictionaries containing page number and text.
    """

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document):

        text = page.get_text()

        pages.append(
            {
                "page": page_number + 1,
                "text": text
            }
        )

    document.close()

    return pages


if __name__ == "__main__":

    PDF_PATH = "data/raw/bnp_paribas_annual_report_2025.pdf"

    pages = load_pdf(PDF_PATH)

    print("Nombre de pages extraites :", len(pages))

    print("\nPremière page :")
    print(pages[0]["text"][:1000])


#PDF BNP Paribas
#      ↓
#PyMuPDF
#      ↓
#936 objets Page
#     ↓
#Extraction du texte
#      ↓
#Conservation des métadonnées
#      ↓
#[
#  {page: 1, text: "..."},
#  {page: 2, text: "..."},
#]