def json_to_text(record: dict) -> str:
    """
    Serialize a single invoice JSON (schema+data) into plain text for embedding.
    """
    lines = []
    for k, v in record.get('data', {}).items():
        lines.append(f"{k}: {v}")
    return "\n".join(lines)