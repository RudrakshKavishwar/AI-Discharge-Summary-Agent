# agents/summary_generator.py

from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_summary(state):

    extracted_data = state.get("extracted_data", "")

    prompt = f"""
You are a clinical discharge summary assistant.

Generate a structured discharge summary containing:

1. Patient Demographics
2. Admission Diagnosis
3. Hospital Course
4. Investigations
5. Procedures
6. Medication Reconciliation
7. Pending Results
8. Discharge Condition
9. Follow-up Instructions
10. Missing Information
11. Conflicts Detected

Rules:
- Never hallucinate.
- If information is missing write MISSING.
- If reports are pending write PENDING.

DATA:

{extracted_data}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["final_summary"] = response.text

    return state