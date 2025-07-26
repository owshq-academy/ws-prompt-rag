from langchain.prompts import PromptTemplate

# 1️⃣ Schema discovery: force JSON-only output in a code fence
INVOICE_SCHEMA_PROMPT = PromptTemplate(
    input_variables=["invoice_text"],
    template="""
You are an expert financial-document analyst.
Extract every distinct data field from this invoice text and build a JSON Schema.

Output **only** valid JSON, nothing else, inside triple backticks.

```json
{{
  "fields": [
    {{
      "name": "<field_name>",
      "type": "<data_type>",
      "description": "<short description>"
    }},
    …
  ]
}}
```

Invoice Text:
{invoice_text}
""".strip(),
)

# 2️⃣ Extraction: force JSON-only output wrapped in backticks
INVOICE_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["invoice_text", "schema_json"],
    template="""
You are an invoice-data extractor.
Given this JSON schema and the invoice text, extract all values into a JSON object that exactly matches the schema.

Output **only** the JSON (no commentary), inside triple backticks:

```json
{schema_json}
```

Invoice Text:
{invoice_text}
""".strip(),
)

# 3️⃣ Project summary: remind the LLM of the workflow and ask next-step suggestion
PROJECT_SUMMARY_PROMPT = PromptTemplate(
    input_variables=[],
    template="""
You are an AI assistant collaborating on a LangChain-based invoice analyzer.

**Project Goals:**
1. Load PDF invoices and extract their raw text.
2. Use a large language model to infer a JSON Schema of all invoice fields.
3. Use the LLM again to extract each field’s value into that schema.
4. Validate, clean, and emit a final JSON representation of the invoice.

**Current Status:**
- We have loaders in `loaders.py` to pull text from PDFs.
- We have two prompts (`INVOICE_SCHEMA_PROMPT` & `INVOICE_EXTRACTION_PROMPT`) wrapped in RunnableSequence pipelines.
- Environment and token limits are configured to avoid truncation.
- Utilities in `utils.py` handle any JSON cleanup and validation.

Using this context, **(a)** give a concise summary of the workflow, and **(b)** suggest one improvement or extension we could build next.
""".strip(),
)
