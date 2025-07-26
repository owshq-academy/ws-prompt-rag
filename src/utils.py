import json


def validate_json_schema(schema_json: str) -> dict:
    """
    Parse and validate that the provided string is a JSON schema with a 'fields' list.
    If the raw string contains extra text or is truncated, extract only the JSON object
    and auto-balance braces before parsing.
    Raises ValueError on invalid JSON or schema structure.
    """
    def _extract_json(s: str) -> str:
        start = s.find('{')
        end   = s.rfind('}')
        if start != -1 and end != -1 and end > start:
            return s[start:end+1]
        return s

    def _balance_braces(s: str) -> str:
        # Append missing closing braces if truncated
        open_count  = s.count('{')
        close_count = s.count('}')
        if open_count > close_count:
            s += '}' * (open_count - close_count)
        return s

    # Step 1: try direct parse
    try:
        schema = json.loads(schema_json)
    except json.JSONDecodeError:
        # Step 2: extract JSON substring and balance braces
        cleaned = _extract_json(schema_json)
        cleaned = _balance_braces(cleaned)
        try:
            schema = json.loads(cleaned)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON schema after cleaning: {e}\nRaw output was:\n{schema_json}")

    # Validate structure
    if not isinstance(schema, dict) or "fields" not in schema or not isinstance(schema["fields"], list):
        raise ValueError("Schema must be a JSON object with a top‐level 'fields' list.")

    for field in schema["fields"]:
        if not all(k in field for k in ("name", "type", "description")):
            raise ValueError("Each field entry must contain 'name', 'type', and 'description'.")

    return schema


def validate_extracted_data(data_json: str, schema: dict) -> dict:
    """
    Parse and validate extracted invoice data against the given schema dict.
    If the raw string contains extra text or is truncated, extract only the JSON object
    and auto-balance braces before parsing.
    Raises ValueError on invalid JSON or missing fields.
    """
    def _extract_json(s: str) -> str:
        start = s.find('{')
        end   = s.rfind('}')
        if start != -1 and end != -1 and end > start:
            return s[start:end+1]
        return s

    def _balance_braces(s: str) -> str:
        open_count  = s.count('{')
        close_count = s.count('}')
        if open_count > close_count:
            s += '}' * (open_count - close_count)
        return s

    # Step 1: try direct parse
    try:
        data = json.loads(data_json)
    except json.JSONDecodeError:
        cleaned = _extract_json(data_json)
        cleaned = _balance_braces(cleaned)
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data after cleaning: {e}\nRaw output was:\n{data_json}")

    # Validate data structure
    if not isinstance(data, dict):
        raise ValueError("Extracted data must be a JSON object.")

    validated = {}
    for field in schema.get("fields", []):
        name = field["name"]
        if name not in data:
            raise ValueError(f"Missing field '{name}' in extracted data.")
        validated[name] = data[name]

    return validated