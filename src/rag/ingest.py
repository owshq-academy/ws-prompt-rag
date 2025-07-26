import json
from pathlib import Path
from langchain.schema import Document
from .configs import RAW_JSON_DIR
from .utils import json_to_text


def load_documents() -> list[Document]:
    docs = []
    for file in Path(RAW_JSON_DIR).glob('*.json'):
        payload = json.loads(file.read_text(encoding='utf-8'))
        text = json_to_text(payload)
        docs.append(Document(page_content=text, metadata={'source': str(file)}))
    return docs