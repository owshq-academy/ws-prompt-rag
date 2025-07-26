import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone.vectorstores import Pinecone as PineconeVectorStore
from src.RAG.configs import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL,
    PINECONE_INDEX_NAME,
    PINECONE_NAMESPACE,
)
from src.RAG.ingest import load_documents

import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

load_dotenv()


def build_retriever(
    embedding_model: str = None,
    use_pinecone: bool = True
):
    """
    Load JSON invoices, split into text chunks, embed them, and build a retriever.

    If `use_pinecone` is True, uses an existing Pinecone index; otherwise falls back to Chroma.
    """
    model = embedding_model or EMBEDDING_MODEL

    # TODO 1) Load and split documents
    docs = load_documents()
    splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(docs)

    # TODO 2) Embedding setup — always use OpenAI embeddings
    emb = OpenAIEmbeddings(model=model)

    # TODO 3) Build vector store
    if use_pinecone:

        pc = Pinecone(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment=os.getenv("PINECONE_ENVIRONMENT")
        )
        pine_index = pc.Index(PINECONE_INDEX_NAME)

        vectordb = PineconeVectorStore(
            pine_index,
            embedding=emb,
            text_key="page_content",
            namespace=PINECONE_NAMESPACE
        )
        vectordb.add_documents(chunks)
    else:
        from langchain.vectorstores import Chroma

        base_dir = Path(__file__).parent / "vectordb"
        vectordb = Chroma.from_documents(
            chunks,
            emb,
            persist_directory=str(base_dir)
        )
        vectordb.persist()

    return vectordb.as_retriever()
