# src/langchain/chains.py

from langchain_openai import ChatOpenAI
from langchain_core.runnables.base import RunnableSequence
from .prompts import INVOICE_SCHEMA_PROMPT, INVOICE_EXTRACTION_PROMPT, PROJECT_SUMMARY_PROMPT


def build_invoice_pipeline(model_name: str = "gpt-4", temperature: float = 0.0, max_tokens: int = 1500):
    """
    Create two pipelines for invoice processing using the Chat API:
    1) schema_seq: infer a JSON schema from invoice text
    2) extract_seq: extract invoice data per schema
    """
    # Use ChatOpenAI for chat completions endpoint
    llm = ChatOpenAI(model_name=model_name, temperature=temperature, max_tokens=max_tokens)

    schema_seq  = RunnableSequence(INVOICE_SCHEMA_PROMPT, llm)
    extract_seq = RunnableSequence(INVOICE_EXTRACTION_PROMPT, llm)
    return schema_seq, extract_seq


def build_summary_pipeline(model_name: str = "gpt-4", temperature: float = 0.0, max_tokens: int = 500):
    """
    Create a pipeline that outputs a project summary and next-step suggestion.
    """
    llm = ChatOpenAI(model_name=model_name, temperature=temperature, max_tokens=max_tokens)
    summary_seq = RunnableSequence(PROJECT_SUMMARY_PROMPT, llm)
    return summary_seq
