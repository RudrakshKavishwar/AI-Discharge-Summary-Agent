import fitz
import os
from PIL import Image
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

pdf_path = r"data\patient_2\patient_2.pdf"

doc = fitz.open(pdf_path)

page = doc[0]

pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

os.makedirs("temp", exist_ok=True)

image_path = "temp/page1.png"

pix.save(image_path)

img = Image.open(image_path)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        "Extract all visible text from this medical document.",
        img
    ]
)

print(response.text)