# tools/conflict_checker.py

def detect_conflicts(extracted_data):

    conflicts = []

    diagnoses = extracted_data.get("diagnoses", [])

    if len(set(diagnoses)) != len(diagnoses):
        conflicts.append(
            "Multiple diagnosis entries differ across notes"
        )

    return conflicts