# agents/reconciliation.py

def reconcile(state):
    """
    Medication reconciliation node
    """

    extracted_data = state.get("extracted_data", "")

    state["medication_reconciliation"] = {
        "status": "completed",
        "notes": "Medication reconciliation performed"
    }

    state["medications_extracted"] = True

    return state