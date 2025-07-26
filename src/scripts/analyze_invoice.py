# src/scripts/analyze_invoice.py

import sys
import os
import json
import re
import shutil
from pathlib import Path
from dotenv import load_dotenv

# ─── Project setup ──────────────────────────────────────────────────────────
here = Path(__file__).resolve()
src_dir = here.parent.parent           # .../ws-prompt-rag/src
project_root = src_dir.parent          # .../ws-prompt-rag

# Load .env for API keys
dotenv_path = project_root / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)
else:
    print(f"⚠️ Warning: .env not found at {dotenv_path}")

# Ensure src_dir on path to import our package
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from src.loaders import load_invoice_text
from src.chains import build_invoice_pipeline
from src.utils import validate_json_schema, validate_extracted_data

def strip_code_fence(text: str) -> str:
    """
    Remove surrounding triple backtick code fences and optional 'json' label.
    """
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
    return match.group(1) if match else text

def process_file(path: Path):
    print(f"\nProcessing invoice: {path.name}")
    text = load_invoice_text(str(path))

    # Build the pipelines
    schema_seq, extract_seq = build_invoice_pipeline()

    # 1) Infer schema from text
    raw_schema_msg = schema_seq.invoke({"invoice_text": text})
    raw_schema = getattr(raw_schema_msg, 'content', raw_schema_msg)
    cleaned_schema = strip_code_fence(raw_schema)
    schema = validate_json_schema(cleaned_schema)

    # 2) Extract data using inferred schema
    raw_data_msg = extract_seq.invoke({
        "invoice_text": text,
        "schema_json": cleaned_schema
    })
    raw_data = getattr(raw_data_msg, 'content', raw_data_msg)
    cleaned_data = strip_code_fence(raw_data)
    data = validate_extracted_data(cleaned_data, schema)

    # 3) Ensure processed directory exists
    raw_dir = path.parent                        # .../src/langchain/data/raw
    processed_dir = raw_dir.parent / "processed"  # .../src/langchain/data/processed
    processed_dir.mkdir(parents=True, exist_ok=True)

    # 4) Write output JSON
    output = {"schema": schema, "data": data}
    json_path = processed_dir / f"{path.stem}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Output written to {json_path}")

    # 5) Move original PDF to processed folder
    dest_pdf = processed_dir / path.name
    shutil.move(str(path), str(dest_pdf))
    print(f"Moved original PDF to {dest_pdf}")

def main():
    raw_dir = src_dir / "data" / "raw"
    if not raw_dir.exists():
        print(f"Error: raw folder not found: {raw_dir}")
        sys.exit(1)

    pdf_files = list(raw_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No invoice PDF files found in {raw_dir}")
        return

    for invoice_path in pdf_files:
        process_file(invoice_path)

if __name__ == "__main__":
    main()