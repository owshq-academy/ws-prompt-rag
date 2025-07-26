from pathlib import Path
import os

RAW_JSON_DIR = Path(__file__).parent.parent / "data" / "processed"

EMBEDDING_MODEL = "text-embedding-ada-002"

VECTORDB_DIR = Path(__file__).parent / "vectordb"

PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "invoices")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "default")
PINECONE_DIMENSION  = int(os.getenv("PINECONE_DIMENSION", "1536"))
PINECONE_METRIC = os.getenv("PINECONE_METRIC", "cosine")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
