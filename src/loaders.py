# src/langchain/loaders.py

import logging
import os
import pdfplumber
import pandas as pd

# silence font warnings
logging.getLogger("pdfminer").setLevel(logging.CRITICAL)
logging.getLogger("pdfplumber").setLevel(logging.CRITICAL)

def load_invoice_text(filepath: str) -> str:
    if not filepath.lower().endswith(".pdf"):
        raise ValueError("Only PDF supported")
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    return text

def load_invoice_table(filepath: str, page_number: int = 0) -> pd.DataFrame:
    """
    Extract the first table on `page_number` as a pandas DataFrame.
    """
    with pdfplumber.open(filepath) as pdf:
        page = pdf.pages[page_number]
        table = page.extract_table()
    if not table:
        return pd.DataFrame()
    # first row is header
    header, *rows = table
    return pd.DataFrame(rows, columns=header)