import fitz

pdf_path = r"data\patient_2\patient_2.pdf"

doc = fitz.open(pdf_path)

print("Pages:", len(doc))

for i, page in enumerate(doc):
    text = page.get_text()
    print(f"Page {i+1}: {len(text)} chars")