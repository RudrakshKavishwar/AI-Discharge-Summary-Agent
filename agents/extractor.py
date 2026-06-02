# agents/extractor.py

from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def extractor(state):

    text = state.get("pdf_text", "")

    if not text:
        state["error"] = "No OCR text found"
        return state

    prompt = f"""
Extract and return JSON only.

Fields:

- demographics
- diagnoses
- procedures
- admission_medications
- discharge_medications
- allergies
- pending_results
- discharge_condition
- followup_instructions
- hospital_course

DOCUMENT:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["extracted_data"] = response.text
    state["extracted"] = True

    return state