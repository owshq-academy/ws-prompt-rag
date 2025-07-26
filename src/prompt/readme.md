# 🧾 Prompt Set for Invoice Extraction – UberEats (LLM-Focused)

This repository contains **7 thoughtfully designed prompts** for structured data extraction from UberEats invoices. Each prompt is tailored to handle varying levels of document complexity — from clean text-based PDFs to scanned images with handwritten text — using different LLM prompting techniques.

---

## 📦 Prompt Inventory

| # | File Name | Strategy | Description |
|---|-----------|----------|-------------|
| 1 | `1-zero-shot.txt` | Zero-Shot | Inference without prior examples |
| 2 | `2-out-sch-def.txt` | Schema Definition | Strict field mapping with schema |
| 3 | `3-few-shot.txt` | Few-Shot | Examples included to guide extraction |
| 4 | `4-cot-persona.txt` | Chain-of-Thought (CoT) | Step-by-step reasoning + persona |
| 5 | `5-ocr-focused-instruction.txt` | OCR-Focused | Emphasizes stylized text/handwriting handling |
| 6 | `6-self-validation-out-constraints.txt` | Self-Validation | Adds rule checks and error detection |
| 7 | `7-inv-extraction-specialist.txt` | Specialist Persona | High-precision, production-ready expert prompt |

---

## 🧠 Detailed Prompt Descriptions

### 1. `1-zero-shot.txt` – Zero-Shot Prompt
**Strategy**: Minimal instruction, no examples.  
**Goal**: Have the model infer how to extract fields purely from directive text.  
**Use Case**: Baseline testing and quick prototyping.

---

### 2. `2-out-sch-def.txt` – Output Schema Definition
**Strategy**: Defines a fixed JSON schema.  
**Goal**: Forces structured outputs with field alignment.  
**Use Case**: When working with contract-driven systems or post-processing validators.

---

### 3. `3-few-shot.txt` – Few-Shot Prompt
**Strategy**: Includes a successful example for the model to learn from.  
**Goal**: Improve extraction reliability by imitation.  
**Use Case**: Recommended when documents are multilingual or follow varied templates.

---

### 4. `4-cot-persona.txt` – Chain-of-Thought Persona
**Strategy**: Uses a role-playing assistant to explain steps before final output.  
**Goal**: Transparency in reasoning with intermediate thoughts.  
**Use Case**: Debugging, research, or model interpretability.

---

### 5. `5-ocr-focused-instruction.txt` – OCR-Focused Prompt
**Strategy**: Addresses documents with handwriting or cursive fonts.  
**Goal**: Ensure no field is skipped due to font/scan artifacts.  
**Use Case**: Scanned or stylized invoices (e.g., handwritten receipts).

---

### 6. `6-self-validation-out-constraints.txt` – Self-Validating Output
**Strategy**: Applies arithmetic and logical checks after data extraction.  
**Goal**: Catch common errors in totals, item calculations, and date formatting.  
**Use Case**: High-confidence pipelines and financial audits.

---

### 7. `7-inv-extraction-specialist.txt` – Invoice Extraction Specialist
**Strategy**: Expert assistant with strict extraction rules.  
**Goal**: Precision with null-return logic for missing fields.  
**Use Case**: Production pipelines or client-facing invoice systems.

---

## ✅ Recommended Pairings

You can combine prompts for improved reliability:

- **CoT + Validation** → `4` + `6`: Enables reasoning **with** rule checking.
- **OCR + Specialist** → `5` + `7`: Best for scanned invoices with accuracy guarantees.

---

## 🚀 Deployment Tip

Use these prompts with any LLM or API (e.g., OpenAI GPT-4, Claude, Gemini) by injecting the prompt content as the system/user input. Set `temperature = 0` for deterministic behavior.

---

## 📂 Folder Structure Suggestion
