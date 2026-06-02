# learning/simulate_training.py

import json
import os

from reviewer import simulated_reviewer
from metrics import edit_score

# Get project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# outputs/discharge_summary.txt
summary_path = os.path.join(
    BASE_DIR,
    "outputs",
    "discharge_summary.txt"
)

print("Reading summary from:")
print(summary_path)

if not os.path.exists(summary_path):
    raise FileNotFoundError(
        f"File not found: {summary_path}"
    )

with open(
    summary_path,
    "r",
    encoding="utf-8"
) as f:

    draft = f.read()

review = simulated_reviewer(draft)

score = edit_score(
    review["draft"],
    review["edited"]
)

# learning/memory.json
memory_path = os.path.join(
    BASE_DIR,
    "learning",
    "memory.json"
)

try:

    with open(
        memory_path,
        "r",
        encoding="utf-8"
    ) as f:

        memory = json.load(f)

except Exception:

    memory = []

memory.append({

    "edits": review["edits"],

    "score": score

})

with open(
    memory_path,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        memory,
        f,
        indent=4
    )

print("\n===== PART 2 RESULTS =====")
print("Score:", score)
print("Edits:", review["edits"])
print("\nMemory updated successfully.")
print(f"Memory file: {memory_path}")