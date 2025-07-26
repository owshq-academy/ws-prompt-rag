# Workshop: Prompt Engineering & RAG (Retrieval-Augmented Generation)

A modular Retrieval-Augmented Generation (RAG) system for document analysis, prompt engineering, and data management. Designed for research, prototyping, and production workflows involving invoices, PDFs, and custom prompts.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Prompt Engineering](#prompt-engineering)
- [Data & Storage](#data--storage)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

## Overview
This repository provides a flexible framework for:
- Document ingestion and processing (PDFs, JSON)
- Retrieval-Augmented Generation (RAG) pipelines
- Custom prompt engineering and evaluation
- Data storage and management
- Extensible chains and loaders for NLP tasks

## Features
- **RAG Pipelines:** Easily ingest, retrieve, and query documents
- **Prompt Library:** Curated prompt templates for zero-shot, few-shot, CoT, and more
- **Invoice Analysis:** Scripts and data for invoice extraction and validation
- **Modular Design:** Organized codebase for easy extension and maintenance
- **Docker Support:** Containerized setup for reproducibility

## Directory Structure
```
├── build/                # Docker and deployment files
│   ├── docker-compose.yml
│   └── data/             # Database and assets
├── prompt/               # Prompt templates and meta-prompt generator
├── src/                  # Source code
│   ├── chains.py         # RAG chains and pipelines
│   ├── loaders.py        # Data/document loaders
│   ├── prompts.py        # Prompt utilities
│   ├── utils.py          # General utilities
│   ├── cnk-emb/          # Embedding and chunking modules
│   ├── data/             # Processed datasets
│   ├── RAG/              # RAG-specific modules
│   └── scripts/          # Analysis scripts
├── storage/              # Raw documents (PDF, PNG)
├── requirements.txt      # Python dependencies
└── readme.md             # Project documentation
```

## Installation
### Prerequisites
- Python 3.8+
- [Docker](https://www.docker.com/get-started) (optional)

### Clone the Repository
```bash
git clone https://github.com/yourusername/ws-prompt-rag.git
cd ws-prompt-rag
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### (Optional) Start with Docker
```bash
cd build
docker-compose up --build
```

## Usage
### Document Ingestion & RAG Pipeline
Run the main RAG pipeline:
```bash
python src/RAG/ingest.py
python src/RAG/qa.py
```

### Invoice Analysis
```bash
python src/scripts/analyze_invoice.py
```

### Embedding & Chunking Demo
```bash
python src/cnk-emb/main.py
```

## Prompt Engineering
Explore and use prompt templates in [`prompt/`](./prompt/):
- `1-zero-shot.txt`: Zero-shot prompt
- `3-few-shot.txt`: Few-shot prompt
- `4-cot-persona.txt`: Chain-of-thought persona prompt
- `meta-prompt-generator.md`: Meta prompt generation guide

## Data & Storage
- **Processed Data:** [`src/data/processed/`](./src/data/processed/)
- **Raw Documents:** [`storage/`](./storage/)
- **Database & Assets:** [`build/data/`](./build/data/)

## Contributing
Contributions are welcome! Please see [CONTRIBUTING.md](#) for guidelines.

## License
Distributed under the MIT License. See [LICENSE](#) for details.

## Links
- [LangChain](https://github.com/langchain-ai/langchain) - RAG framework inspiration
- [Docker Documentation](https://docs.docker.com/)
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)

---
For questions or support, open an issue or contact the maintainer.
