# agents/gemini_ocr.py

from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import os
import time

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_page_text(image_path):
    """
    OCR extraction using Gemini Vision
    """

    max_retries = 3

    for attempt in range(max_retries):

        try:

            image = Image.open(image_path)

            response = model.generate_content([
                """
                Extract ALL visible medical text exactly.

                Preserve:
                - Diagnoses
                - Medications
                - Lab values
                - Tables
                - Dates
                - Doctor notes
                - Discharge summaries
                - Investigation reports

                Do not summarize.
                Return only extracted text.
                """,
                image
            ])

            # Free-tier protection
            time.sleep(12)

            return response.text

        except Exception as e:

            error_msg = str(e)

            if "429" in error_msg:

                wait_time = 30 * (attempt + 1)

                print(
                    f"Rate limit hit. Waiting {wait_time} seconds..."
                )

                time.sleep(wait_time)

                continue

            print(f"OCR Error on {image_path}: {e}")

            return ""

    print(f"Failed OCR after {max_retries} retries")

    return ""