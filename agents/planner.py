# agents/planner.py

def planner(state):

    tasks = []

    if not state.get("extracted"):
        tasks.append("extract_data")

    tasks.append("reconcile_meds")
    tasks.append("validate")
    tasks.append("generate_summary")

    state["plan"] = tasks

    return state