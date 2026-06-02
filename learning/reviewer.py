import json

def simulated_reviewer(summary):

    edits = []

    corrected = summary

    if "Patient Demographics" in summary and "MISSING" in summary:
        edits.append(
            "Patient demographics section incomplete"
        )

    if "Allergies" not in summary:
        edits.append(
            "Allergy section missing"
        )

    if "Discharge Condition" not in summary:
        edits.append(
            "Discharge condition missing"
        )

    return {
        "draft": summary,
        "edited": corrected,
        "edits": edits
    }