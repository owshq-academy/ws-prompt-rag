# src/RAG/configs.py

from pathlib import Path
import os

# Folder containing JSON outputs from invoice analyzer
RAW_JSON_DIR = Path(__file__).parent.parent / "data" / "processed"

# Embedding model settings
EMBEDDING_MODEL = "text-embedding-ada-002"

# Vector store persistence directory for Chroma fallback
VECTORDB_DIR = Path(__file__).parent / "vectordb"

# Pinecone configuration
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "invoices")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "default")
PINECONE_DIMENSION  = int(os.getenv("PINECONE_DIMENSION", "1536"))
PINECONE_METRIC = os.getenv("PINECONE_METRIC", "cosine")

# Text splitter parameters
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
