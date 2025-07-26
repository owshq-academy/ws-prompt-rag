import os
from pdfminer.high_level import extract_text
from utils.chunking_strategies import (
    fixed_size_chunking,
    recursive_char_split,
    semantic_chunking,
    language_based_chunking,
    context_aware_chunking
)


def load_pdf_text(pdf_path):
    return extract_text(pdf_path)


def preview_chunks(name, chunks, n=3):
    print(f"\n{name} (showing {n} chunks):")
    for i, chunk in enumerate(chunks[:n]):
        print(f"\n--- Chunk {i+1} ---\n{chunk[:300]}...\n")

if __name__ == "__main__":
    pdf_path = "data/doc-datasets.pdf"
    text = load_pdf_text(pdf_path)

    fs_chunks = fixed_size_chunking(text)
    rc_chunks = recursive_char_split(text)
    sem_chunks = semantic_chunking(text)
    lb_chunks = language_based_chunking(text, by="paragraph")
    ca_chunks = context_aware_chunking(text)

    preview_chunks("Fixed Size Chunking", fs_chunks)
    preview_chunks("Recursive Character Split", rc_chunks)
    preview_chunks("Semantic Chunking", sem_chunks)
    preview_chunks("Language-Based (Paragraph) Chunking", lb_chunks)
    preview_chunks("Context-Aware Chunking", ca_chunks)
