# agents/validator.py

def validator(state):
    """
    Validation node
    Checks for missing fields and conflicts
    """

    extracted_data = state.get("extracted_data", "")

    missing_fields = []

    if not extracted_data:
        missing_fields.append("No extracted data")

    state["missing_fields"] = missing_fields

    state["conflicts_detected"] = False

    return state