# tools/medication_tool.py

def compare_medications(admission_meds, discharge_meds):

    changes = []

    for med in discharge_meds:

        if med not in admission_meds:

            changes.append({
                "medication": med,
                "change_type": "ADDED",
                "reason": "NOT DOCUMENTED"
            })

    for med in admission_meds:

        if med not in discharge_meds:

            changes.append({
                "medication": med,
                "change_type": "STOPPED",
                "reason": "NOT DOCUMENTED"
            })

    return changes