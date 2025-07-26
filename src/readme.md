# Invoice Analyzer Application

A LangChain-powered Python tool that automates PDF invoice processing end-to-end:

1.	Extract text from PDF invoices
2.	Infer a JSON schema of all invoice fields using an LLM
3.	Extract structured data per the schema via an LLM
4.	Validate and clean the JSON output
5.	Save results as JSON and move processed PDFs

---

### 🚀 Features
- PDF Parsing: Uses pdfplumber to pull raw text from single-page invoices.
- Schema Inference: Prompts a chat LLM (gpt-4 by default) to discover all fields and types.
- Data Extraction: Uses the inferred schema to extract values into a deterministic JSON object.
- Automatic Validation: Strips code fences, auto-balances braces, and enforces schema structure.
- File Management: Outputs <invoice>.json in data/processed/ and moves the original PDF there.
- Extensible: Ready for RAG pipelines with vector stores and embedding libraries installed.

---

### 📂 Project Structure
```sh
ws-prompt-rag/
├── .env                       # OPENAI_API_KEY
├── README.md                  # This documentation
├── requirements.txt           # Python dependencies
└── src/
    ├── langchain/             # Core package modules
    │   ├── prompts.py         # LLM PromptTemplates
    │   ├── loaders.py         # PDF text loader
    │   ├── chains.py          # RunnableSequence builders
    │   └── utils.py           # JSON cleanup & validation
    └── scripts/
        └── analyze_invoice.py # Main script: processes data/raw → data/processed
```

- data/raw/: Drop new PDF invoices here.
- data/processed/: Receives JSON outputs and moved PDFs.

---

1. Install dependencies
```sh
pip install –upgrade pip
pip install -r requirements.txt
```

2. Configuration

Create a .env at the project root:
```sh
OPENAI_API_KEY=sk-...YOUR_API_KEY...
```

3. Usage
	1.	Drop one or more PDF invoices into src/langchain/data/raw/.
	2.	Run the analyzer:

```sh
python src/scripts/analyze_invoice.py
```

4. **Inspect** results in `src/langchain/data/processed/`:  
- `<invoice>.json` containing `schema` and `data` keys  
- Original PDFs moved alongside JSON

---

### 📦 Requirements

```txt
langchain>=0.2.0
langchain-core>=0.2.0
langchain-openai>=0.1.0
pdfplumber>=0.9.0
python-dotenv>=1.0.1
```
Plus optional vector/embeddings libs for RAG.

---
### 🗂️ Code Overview
- prompts.py: Defines three PromptTemplates:
  - INVOICE_SCHEMA_PROMPT
  - INVOICE_EXTRACTION_PROMPT
  - PROJECT_SUMMARY_PROMPT
- loaders.py: Provides load_invoice_text() using pdfplumber.
- chains.py: Exposes:
  - build_invoice_pipeline() → (schema_seq, extract_seq)
  - build_summary_pipeline() → summary_seq
- utils.py: Contains JSON cleaning & validation helpers.
- analyze_invoice.py: 
- Orchestrates:
	1.	Loading environment
	2.	Iterating over data/raw/*.pdf
	3.	LLM schema → data extraction
	4.	JSON output + file move

---

### 🔮 Next Steps & RAG Readiness
- Integrate a vector store (Chroma, Pinecone, etc.) and text splitters for multi-page or multi-document RAG.
- Add CLI flags via typer for custom output directories, model parameters, or dry runs.
- Implement caching of LLM calls to reduce API costs and speed up processing.
