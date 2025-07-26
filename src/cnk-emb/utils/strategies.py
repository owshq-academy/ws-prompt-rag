import re
import nltk
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt")


def fixed_size_chunking(text, chunk_size=500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def recursive_char_split(text, chunk_size=500, overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return splitter.split_text(text)


def semantic_chunking(text, chunk_size=5):
    sentences = sent_tokenize(text)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)

    chunks = []
    current_chunk = []
    for i in range(len(sentences)):
        current_chunk.append(sentences[i])
        if len(current_chunk) >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks


def language_based_chunking(text, by="paragraph"):
    if by == "sentence":
        return sent_tokenize(text)
    elif by == "word":
        return word_tokenize(text)
    elif by == "paragraph":
        return text.split("\n\n")
    else:
        raise ValueError("Unsupported chunk type")


def context_aware_chunking(text, max_chunk_length=600, stride=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), stride):
        chunk = words[i:i + max_chunk_length]
        if chunk:
            chunks.append(" ".join(chunk))
    return chunks
